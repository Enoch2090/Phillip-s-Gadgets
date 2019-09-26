from config import Config
import glob,shutil,datetime,os


def newTaskpaper():
	f = open('settings.cfg')
	cfg = Config(f)
	f.close()
	newFileName = str(datetime.date.today()).replace('-', ':')
	srcDirectory = glob.glob(cfg.fileDirectory + '/' + '*.taskpaper')[-1]
	dstDirectory = cfg.fileDirectory + '/' + newFileName + '.taskpaper'
	arcDir = cfg.archiveDirectory + '/' + str(datetime.date.today().year) + '/' + str(datetime.date.today().month)
	arcDirectory = srcDirectory.replace(cfg.fileDirectory, arcDir)
	print(arcDir)
	shutil.copyfile(srcDirectory, dstDirectory)
	if not os.path.isdir(arcDir):
	    os.makedirs(arcDir,mode=0o777)
	shutil.move(srcDirectory, arcDirectory)

	r = open(dstDirectory,'r')
	lines = r.readlines()
	lastRemoved = False
	lastIndent = 0
	lastAsTask = False
	thisAsTask = True
	newLines = []
	for line in lines:
		removeThis = False
		thisIndent = 0
		for char in line: # Count indent
			if char == '\t':
				thisIndent += 1

		if line.find('- ')!=-1:
			thisAsTask = True
		else:
			thisAsTask = False

		if thisIndent > lastIndent and lastRemoved:
			removeThis = True
		elif thisIndent >= lastIndent and not(thisAsTask) and not(lastAsTask) and lastIndent >= 1:
			removeThis = True

		if line.find('@done')!=-1 or line.find('@discarded')!=-1 or removeThis:
			removeThis = True
		else:
			newLines += line
		
		lastAsTask = thisAsTask
		lastRemoved = removeThis
		lastIndent = thisIndent

	r.close()
	w = open(dstDirectory,'w')
	for line in newLines:
		w.write(line)
	w.close()

	return 1

f = open('settings.cfg')
cfg = Config(f)
f.close()
print('Mode: ' + str(cfg.runMode))
if str(cfg.runMode) == 'newTaskpaper':
	res = newTaskpaper()
	if res == 1:
		print("Succeed")
	else:
		print("Error")
