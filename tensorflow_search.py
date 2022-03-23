import os
import csv
import sys
import pickle
from collections import namedtuple
from datetime import datetime
import numpy as np
import apache_beam as beam
from apache_beam.transforms import util
import tensorflow as tf
import tensorflow_hub as hub
import annoy
from sklearn.random_projection import _gaussian_random_matrix


class TensorSemanticSearch:
    _embed_fn = None

    def __init__(self):
        self.prepare_data()

    def prepare_data(self):
        with open('summaries.txt', 'w', encoding='cp1251') as output:
            with open('fetched_data.csv', 'r', encoding='cp1251') as f:
                csv_reader = csv.reader(f)
                for line in csv_reader:
                    if line:
                        output.write(f"{'^'.join(line[1:])}\n")

    def generate_embeddings(self, text, model_url, random_projection_matrix=None):
        # Beam will run this function in different processes that need to
        # import hub and load embed_fn (if not previously loaded)
        if self._embed_fn is None:
            self._embed_fn = hub.load(model_url)
        embedding = self._embed_fn(text).numpy()
        if random_projection_matrix is not None:
            embedding = embedding.dot(random_projection_matrix)
        return text, embedding

    def to_tf_example(self, entries):
        examples = []

        text_list, embedding_list = entries
        for i in range(len(text_list)):
            text = text_list[i]
            embedding = embedding_list[i]

            features = {
                'text': tf.train.Feature(
                    bytes_list=tf.train.BytesList(value=[text.encode('cp1251')])),
                'embedding': tf.train.Feature(
                    float_list=tf.train.FloatList(value=embedding.tolist()))
            }

            example = tf.train.Example(
                features=tf.train.Features(
                    feature=features)).SerializeToString(deterministic=True)

            examples.append(example)

        return examples

    def run_hub2emb(self, args):
        '''Runs the embedding generation pipeline'''

        options = beam.options.pipeline_options.PipelineOptions(**args)
        args = namedtuple("options", args.keys())(*args.values())

        with beam.Pipeline(args.runner, options=options) as pipeline:
            (
                    pipeline,
                    beam.io.ReadFromText(file_pattern=args.data_dir),
                    util.BatchElements(min_batch_size=args.batch_size,
                                       max_batch_size=args.batch_size),
                    beam.Map(self.generate_embeddings, args.model_url, args.random_projection_matrix),
                    beam.FlatMap(self.to_tf_example),
                    beam.io.WriteToTFRecord(file_path_prefix='{}/emb'.format(args.output_dir),
                                            file_name_suffix='.tfrecords')
            )
