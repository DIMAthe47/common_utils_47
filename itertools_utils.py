import itertools
from functools import partial
import numpy as np


def chunkify(iterable_, chunk_size, numpy_array_chunks=True):
    if chunk_size == -1:
        chunk = tuple(iterable_)
        chunks_stream = [chunk]
    else:
        tw = itertools.takewhile
        count = itertools.count
        islice = itertools.islice
        it_iter = iter(iterable_)
        # print(next(it_iter).shape)
        # for i in it_iter:
        #     print(i.shape)
        chunks_stream = tw(bool, (tuple(islice(it_iter, chunk_size)) for _ in count()))
    # chunks_stream = tee_print_iterable(chunks_stream)
    for chunk_stream in chunks_stream:
        print(chunk_stream)
        print(np.array(chunk_stream,copy=False).shape)

    if numpy_array_chunks:
        chunks_stream = map(partial(np.array, copy=False), chunks_stream)
    # chunks_stream = tee_print_iterable(chunks_stream)
    return chunks_stream


def tee_print_iterable(iterable_, shape_only=True):
    iterable_, iterable_copy = itertools.tee(iterable_)
    for i in iterable_copy:
        if isinstance(i, np.ndarray) and shape_only:
            print(i.shape)
        else:
            print(i)
    return iterable_
