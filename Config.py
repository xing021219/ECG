#coding:utf-8

# 图片及视频检测结果保存路径
save_path = 'save_data'

# 使用的模型路径
model_path = 'models/best.pt'

# 检测类别的英文名称
names = {0: 'Left Bundle Branch Block', 1: 'Normal', 2: 'Premature Atrial Contraction', 3: 'Premature Ventricular Contractions', 4: 'Right Bundle Branch Block', 5: 'Ventricular Fibrillation'}

# 检测类别的中文名称
CH_names = ['左束支传导阻滞','心率正常','房性早搏','室性早搏','右束支传导阻滞','心室颤动']

# 报警音路径
alarm_path = 'alarm.wav'

