from django.shortcuts import render,redirect
from django.http import HttpResponse
from textblob import TextBlob
from digifest.models import Reviews
#from django.contrib.auth.forms import UserCreationForm
#from digifest.forms import UserRegistrationForm 
from django.contrib import messages
from .models import UserRegist
from django.template import loader
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords 
# import nltk
#from digifest.dictonary import 
from digifest import dictonary
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create your views here.

reviews=["his organisation has a good plans and policies and all are very easy to understand.",
	"Sold my kidney to buy this, I am now in the hospital on dialysis and using this beautiful product. Just go for it, you won't regret it.",
	"Very bad product .For this price go and buy a gaming laptop.Dell inspiron 15 gaming laptop is better than this garbage",
	"he 15.4 inch 512 gig ssd has radeon pro 560x graphics card not 555x only 256 gig model has 555x card",
	"overpriced.... You could find a better windows laptop at 1/5 th of the price. Go for it only if you have no idea on how to spend 2.2 lakhs"]

def index(request):
	return render(request,'index.html')

def citpage(request):
	const=['secunderabad','sanathnagar','hyderabad']


	const1={
	'con1':const
	}
	return render(request,'vote.html',const1)

def log(request):
	# temp1=loader.get_template('pol_log.html')
	# return HttpResponse(temp1.render())
	return render(request, 'pol_log.html')

def signup(request):
	return render(request,'signup.html')

def manifest(request):
	return render(request,'mainifest.html')


def result(request):
	'''reviews=["his organisation has a good plans and policies and all are very easy to understand.",
		"Sold my kidney to buy this, I am now in the hospital on dialysis and using this beautiful product. Just go for it, you won't regret it.",
		"Very bad product .For this price go and buy a gaming laptop.Dell inspiron 15 gaming laptop is better than this garbage",
		"he 15.4 inch 512 gig ssd has radeon pro 560x graphics card not 555x only 256 gig model has 555x card",
		"overpriced.... You could find a better windows laptop at 1/5 th of the price. Go for it only if you have no idea on how to spend 2.2 lakhs"]
'''
	
	sr=[]
	sr1=[]
	#sr3=[]
	sr2=[]
	k=0

	for j in Reviews.objects.all():
		
		sr2.append(j.ConstituencyName)
		#print("sr2 is",sr2)
		#print(j.ConstituencyName)
		ri1=request.POST.get('retcon',False)
		#print("ri1 is ",ri1)
		if sr2[k]==ri1:
			#print("hi")
			sr1.append(j.reviews)
			#print("k value is",k)
		k=k+1
	sr3=sr1.copy()
		#print(len(sr1))

	'''
	for i in range(0,len(sr1)):
		no=[c for c in sr1[i] if c not in string.punctuation]
		print('before',no)
		no=''.join(no)
		#print('after',no)
		no=no.split()
		print(no)
		no=[word for word in no if word not in stopwords.words('english')]
		sr1[i]=' '.join(no)
		print('hi',sr1[i])
	'''
	'''
	sid=SentimentIntensityAnalyzer()
	for i in sr1:
		ss=sid.polarity_scores(i)
		print('stmt',i,ss)

	print('using tb')
	
	for i in range(0,len(sr1)):
		t=TextBlob(sr1[i])
		s=t.sentiment.polarity
		print(sr1[i],'polarity is',s)
		if s>0:
			sr.append('Positive')
	    #elif s<0:
	    	#sr.append('Negative')
		else:
			sr.append('Negative')
	'''
	

	final_pos=[]
	final_neg=[]

	for i in range(0,len(sr1)):
		pos=0
		neg=0
		rev=sr1[i]
	    #print('review is',rev)
		rev1=[j for j in sr1[i] if j not in string.punctuation]
	    #rev1=[j for j in sr1[i] if j not in string.punctuation]
		rev1=''.join(rev1)
	    #print(rev1)
		rev1=rev1.split()
		rev2=[word for word in rev1 if word not in stopwords.words('english')]
	    #print(rev2)
	    #rev=' '.join(rev2)
		for h in rev2:
			h=h.lower()
			l1=h[0]
			#print('l1 is',l1)
			'''
			if h.startswith(l1):
				if h in h[0]:
					pos+=1
				else:
					neg+=1
			'''
			
			if h.startswith(l1):
				if l1=='a':	
					if h in dictonary.pos_dict_a:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_a:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)

				elif l1=='b':
					if h in dictonary.pos_dict_b:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_b:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
				
				elif l1=='c':
					if h in dictonary.pos_dict_c:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_c:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='d':
					if h in dictonary.pos_dict_d:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_d:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='e':
					if h in dictonary.pos_dict_e:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_e:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='f':
					if h in dictonary.pos_dict_f:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_f:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='g':
					if h in dictonary.pos_dict_g:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_g:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='h':
					if h in dictonary.pos_dict_h:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_h:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='i':
					if h in dictonary.pos_dict_i:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_i:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='j':
					if h in dictonary.pos_dict_j:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_j:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='k':
					if h in dictonary.pos_dict_k:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_k:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='l':
					if h in dictonary.pos_dict_l:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_l:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='m':
					if h in dictonary.pos_dict_m:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_m:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='n':
					if h in dictonary.pos_dict_n:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_n:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='o':
					if h in dictonary.pos_dict_o:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_o:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='p':
					if h in dictonary.pos_dict_p:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_p:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='q':
					if h in dictonary.pos_dict_q:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_q:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='r':
					if h in dictonary.pos_dict_r:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_r:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='s':
					if h in dictonary.pos_dict_s:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_s:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='t':
					if h in dictonary.pos_dict_t:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_t:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='u':
					if h in dictonary.pos_dict_u:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_u:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='v':
					if h in dictonary.pos_dict_v:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_v:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='w':
					if h in dictonary.pos_dict_w:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_w:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='x':
					if h in dictonary.pos_dict_x:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_x:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
			
				elif l1=='y':
					if h in dictonary.pos_dict_y:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_y:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
				
				elif l1=='z':
					if h in dictonary.pos_dict_z:
						pos+=1
			            #print('pos in pos is',pos)
			            #print('neg in pos is',neg)
					elif h in dictonary.neg_dict_z:
						neg+=1
			            #print('pos in neg is',pos)
			            #print('neg in neg is',neg)
	            
		if pos>neg:
			final_pos.append(rev)
		else:
			final_neg.append(rev)


	'''			
	j=0
	positive=[]
	negative=[]
	for i in sr:
		if i=='Positive':
			positive.append(sr3[j])
			j=j+1
		elif (i=='Negative') or (i=='Neutral'):
			negative.append(sr3[j])
			j=j+1
	'''
	



	con={
		'review':sr3,
		'pos':final_pos,
		'neg':final_neg,
		#'con1':const

	}
	k=0
	comm_words=' '
	#print(positive)
	for k in final_pos:
		#print(k)
		token=k.split()
		#print(token)
		for i in range(len(token)):
			token[i]=token[i].lower()
		for word in token:
			comm_words=comm_words+word+' '

	wordcloud=WordCloud(width=500,height=400,min_font_size=10).generate(comm_words)
	fig=plt.figure(figsize=(6,4))
	plt.imshow(wordcloud)
	#plt.axis("off")
	fig.savefig('digifest/static/img/pos_plot.jpg')



	k=0
	comm_words1=' '
	#print(positive)
	for k in final_neg:
		#print(k)
		token=k.split()
		#print(token)
		for i in range(len(token)):
			token[i]=token[i].lower()
		for word in token:
			comm_words1=comm_words1+word+' '

	wordcloud=WordCloud(width=500,height=400,min_font_size=6).generate(comm_words1)
	fig=plt.figure(figsize=(6,4))
	plt.imshow(wordcloud)
	#plt.axis("off")
	fig.savefig('digifest/static/img/neg_plot.jpg')



	return render(request,'result.html',con)	

def register(request):
	
	'''if request.method=='POST':
		form = UserRegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Acoount creates for {username}')
			return redirect('home')
	else:
		form=UserRegistrationForm()'''
	if request.method == "POST":
		first=request.POST["fname"]
		last=request.POST["lname"]
		uname=request.POST["uname"]
		emailid=request.POST["email"]
		passw=request.POST["pass"]
		cpassw=request.POST["cpass"]

		user=UserRegist(fname=first,lname=last,username=uname,email=emailid,password=passw,cpassword=cpassw)
		user.save()
		return redirect('home')

	else:
		return redirect('signup.html')

def logged(request):

	if request.method == "POST":
		
		#use=UserRegist.objects.all()
		
		const=['secunderabad','sanathnagar','hyderabad']

		const1={
		'const2':const
		}


		for i in UserRegist.objects.all():
			email1=i.email
			passw=i.password

			if (email1==request.POST["username1"]) and (passw==request.POST["password1"]):
				return render(request,'mainifest.html',const1)
		return render(request,'hi.html')

	else:
		return render(request, 'mainifest.html')
	

def ins_rev(request):


	if request.method=="POST":
		cn=request.POST['selconst']
		repro=request.POST['yp']

		revi=Reviews(ConstituencyName=cn,reviews=repro)
		revi.save()
		return HttpResponse("<h3>Successfully Sent!</h3>")
	else:
		return redirect('vote.html')





'''
def con_list(request):

	const=['secunderabad','sanathnagar','hyderabad']


	const1={
	'con1':const
	}
	return render(request,'vote.html',const1)
'''

'''
def mani_list(request):
	

		const=['secunderabad','sanathnagar','hyderabad']

		const1={
		'son':const
		}

		return render(request,'')
'''
def ind(request):
	return redirect('index.html')

def problem(request):
	return redirect('index.html')

def list(request):
	sr=[]
	sr1=[]
	for j in Reviews.objects.all():
		sr.append(j.reviews)
		if len(sr)>22:
			# print(len(sr))
			sr1.append(j.reviews)
			

	conlist={
	'list1':sr1
	}

	return render(request,'result1.html',conlist)