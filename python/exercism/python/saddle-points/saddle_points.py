def saddle_points(matrix):
  if len(set(map(len, matrix))) > 1:
      raise ValueError("Irregular matrix!")
  cols = list(zip(*matrix))
  out = []
  for row_idx, row in enumerate(matrix):
    for col_idx, el in enumerate(row):
      if el == max(row) and el == min(cols[col_idx]):
        out.append({"row" : row_idx+1, "column" : col_idx+1})
  return out