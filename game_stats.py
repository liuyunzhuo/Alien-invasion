class GameStats():
	# ������Ϸ��ͳ����Ϣ
	
	def __init__(self, ai_settings):
		# ��ʼ��ͳ����Ϣ
		self.ai_settings = ai_settings
		self.reset_stats()
		# ��Ϸ������ʱ���ڻ״̬
		self.game_active = False
		# ���κ�����¶���Ӧ��������ߵ÷�
		self.high_score = 0
		self.level = 1
		
	def reset_stats(self):
		# ��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0
	
