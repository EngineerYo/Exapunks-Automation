from collections import deque

class Move:
	def __init__(self, dest_rank_id, from_rank_id):
		self.dest_rank_id = dest_rank_id
		self.from_rank_id = from_rank_id

	def output(self):
		out_str = ''
		out_str += str(self.from_rank_id)
		out_str += ' -> '
		out_str += str(self.dest_rank_id)

		print(out_str)