
import random

capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for i in range(35):
   quizfile=open('captialsquiz%s.txt' % (i+1),'w')
   #print(quizfile)
   answerKeyFile=open('capitalsquiz_answers%s.txt'%(i+1),'w')
   
   quizfile.write('Name: \n\nDate: \n\nPeriod: \n\n')

   x="State Capitals Quiz Form %s" %(i+1)
   quizfile.write(x)
   
   quizfile.write('\n\n')

   states=list(capitals.keys())
   random.shuffle(states)

   correct_answer=capitals[states[i]]
   wrong_answer=list(capitals.values())
   del wrong_answers[wrong_answers.index(correct_answer)]
   wrong_answers=random.sample(wrong_answers, 3)
   answer_options=wrong_answers+[correct_answer]
   random.shuffle(answer_options)

   quizfile.write('%s. What is the capital of %s?\n'%(i+1, states[i]))
   for j in range(4):
      quizfile.write('%s. %s\n' % ('ABCD'[j], answer_options[j]))
   quizfile.write('\n')

   answerKeyFile.write('%s. %s\n' %(i+1, 'ABCD'[answer_options.index(correct_answer)]))

   quizfile.close()
   answerKeyFile.close()
         