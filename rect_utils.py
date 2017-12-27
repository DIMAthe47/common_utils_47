def gen_slice_rect(rect_size, tile_size, tile_step):
    # tiles_rects = []
    x, y = (0, 0)
    rect_width, rect_height = rect_size
    tile_width, tile_height = tile_size
    x_step, y_step = tile_step
    while y < rect_height:
        while x < rect_width:
            w = min((tile_width, rect_width - x))
            h = min((tile_height, rect_height - y))
            rect = (x, y, w, h)
            yield rect
            # tiles_rects.append((x, y, w, h))
            x += x_step
        x = 0
        y += y_step

        # print("rect_size", rect_size)
        # print("rects_sliced", tiles_rects)


def gen_slice_rect_n(rect_size, columns, rows):
    # tiles_rects = []
    x, y = (0, 0)
    rect_width, rect_height = rect_size
    tile_width, tile_height = rect_width / columns, rect_height / rows
    x_step, y_step = tile_width, tile_height
    while y < rect_height:
        while x < rect_width:
            w = min((tile_width, rect_width - x))
            h = min((tile_height, rect_height - y))
            rect = (x, y, w, h)
            yield rect
            # tiles_rects.append((x, y, w, h))
            x += x_step
        x = 0
        y += y_step


def get_n_columns_n_rows_for_tile_size(rect_size, tile_size):
    n_columns = rect_size[0] / tile_size[0]
    n_rows = rect_size[1] / tile_size[1]
    if tile_size[0] * n_columns < rect_size[0]:
        n_columns += 1
    if tile_size[1] * n_rows < rect_size[1]:
        n_rows += 1
    return n_columns, n_rows
