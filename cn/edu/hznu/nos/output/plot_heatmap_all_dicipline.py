from pyecharts import HeatMap
import pandas as pd

def heatmap_layout_all():

	axis_name = []
	axis_name_desciption = []
	data = []

	for line in open('/home/lilixia/Documents/task/inter_citation_weight_all.txt'):
		data_item = []
		line_split = line.split('\t')
		for i in range(2):
			term_split = line_split[i].split(' ')
			if len(term_split) > 1:
				term = str(term_split[0])[:1].upper() + str(term_split[1])[:1].upper()
			else:
				term = str(term_split[0])[:4]
			if term not in axis_name:
				axis_name_desciption.append(line_split[i])
				axis_name.append(term)
			data_item.append(term)
		data_item.append(float(line_split[2])*100)
		data.append(data_item)

	file_data = pd.DataFrame({'axis_name_desciption':axis_name_desciption, 'axis_name':axis_name})
	file_data.to_csv('/home/lilixia/Documents/task/all_description.csv', sep=';', header=True, index=False)

	heatmap = HeatMap()
	heatmap.add("Interdiscipline Relationship(ALL)", axis_name, axis_name, data, is_visualmap=True, visual_orient="horizontal", )
	heatmap.render("Interdiscipline_Relationship(ALL).html")

	print(axis_name)
	print(axis_name_desciption)

def heatmap_layout_test(file_name, save_name):

	axis_name = []
	axis_name_desciption = []
	data = []

	file_name = '/home/lilixia/Documents/task/' + file_name + '.txt'
	for line in open(file_name):
		data_item = []
		line_split = line.split('\t')
		for i in range(2):
			term_split = line_split[i].split(' ')
			if len(term_split) > 1:
				term = str(term_split[0])[:1].upper() + str(term_split[1])[:1].upper()
			else:
				term = str(term_split[0])[:4]
			if term not in axis_name:
				axis_name.append(term)
			data_item.append(term)
		data_item.append(float(line_split[2])*100)
		data.append(data_item)

	heatmap = HeatMap()
	heatmap.add(save_name, axis_name, axis_name, data, is_visualmap=True, visual_orient="horizontal", )
	save_name = save_name + '.html'
	heatmap.render(save_name)

if __name__ == '__main__':

	heatmap_layout_all()
	heatmap_layout_test("inter_citation_weight_all_1800_1900", "Interdiscipline_Relationship(1800_1900)")
	heatmap_layout_test("inter_citation_weight_all_1900_1950", "Interdiscipline_Relationship(1900_1950)")
	heatmap_layout_test("inter_citation_weight_all_1920_2017", "Interdiscipline_Relationship(1920_2017)")
	heatmap_layout_test("inter_citation_weight_all_1950_2017", "Interdiscipline_Relationship(1950_2017)")