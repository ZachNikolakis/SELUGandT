import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import argparse

def plot_reads_v_qual(min_dat, x, outputfile):
	qual1 = min_dat.quals[x]
	lookup = {'!':'0','"':'1','#':'2','$':'3','%':'4','&':'5','\'':'6','(':'7',')':'8','*':'9','+':'10',',':'11','-':'12','.':'13','/':'14','0':'15','1':'16','2':'17','3':'18','4':'19','5':'20','6':'21','7':'22','8':'23','9':'24',':':'25',';':'26','<':'27','=':'28','>':'29','?':'30','@':'31','A':'32','B':'33','C':'34','D':'35','E':'36','F':'37','G':'38','H':'39','I':'40', '\n':'0', '\t':'0'}

	new_list = []
	for i in qual1:
		value = lookup[i]
		new_list.append(value)
	labels = range(0, len(qual1))

	new_df = pd.DataFrame(list(zip(labels, new_list)),columns=["position","score"])
	new_df[['score']] = new_df[['score']].apply(pd.to_numeric)
	fig = plt.figure()
	new_df.plot.scatter(x='position', y='score')
	plt.savefig(str(outputfile) + '/' + str(index))
	plt.close()

    
if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("--data", help="Path to the TSV or CSV file containing your data.")
	parser.add_argument("--output", help="Path to directory where you'd like to write the plot files")
	args = parser.parse_args()
	if args.data:
		dataf = args.data
	if args.output:
		outfile = args.output	
	df = pd.read_csv(dataf, delimiter="\t")	
	for index, row in df.iterrows():
		plot_reads_v_qual(df, index, outfile)	
