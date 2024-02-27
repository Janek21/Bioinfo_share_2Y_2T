
def trace(M, seq1, seq2, j, i, res1= [], res2=[]):
	if (i,j) == (0,0):
		return (''.join(reversed(res1)), ''.join(reversed(res2)))
	
	match = M[i-1][j-1]	
	gap = M[i-1][j]
	mismatch = M[i][j-1]

	if match >= max(mismatch,gap):
		res1.append(seq1[j])
		res2.append(seq2[i])
		return trace(M,seq1,seq2, j-1, i-1, res1,res2)
	elif gap <= mismatch: 
		res1.append(seq1[j])
		res2.append('-')
		return trace(M,seq1,seq2, j-1, i, res1,res2)	
	else:	
		res1.append('-')
		res2.append(seq2[i])
		return trace(M,seq1,seq2, j, i-1, res1,res2)	


def nw(seq1, seq2, match, mismatch, gap):

	# Initalize seqs
	seq1 = '-'+seq1
	seq2 = '-'+seq2

	# Initialize matrix
	M = [[-x if y == 0 else -y if x == 0 else 0 for x in range(len(seq1))]  for y in range(len(seq2))]

	for i in range(1,len(seq2)):
		for j in range(1,len(seq1)):
			pos_m = M[i-1][j-1]	
			pos_g = M[i-1][j]
			pos_mis = M[i][j-1]

			if seq1[j] == seq2[i]:
				M[i][j] = pos_m + match
			else: 
				mis_value = max(gap,mismatch)
				
				M[i][j] = max(pos_mis + mis_value, pos_g + mis_value, pos_m + mis_value)

	return M, seq1,seq2


result, seq1, seq2 = nw('THEFASTCAT', 'THERAT', 1, -8, -4)

result_trace = trace(result, seq1, seq2, len(seq1)-1, len(seq2)-1)

def print_alignment(result_trace):
	score = []
	score_total = 0
	for y in range(len(result_trace[0])):
		if '-' in (result_trace[0][y],result_trace[1][y]):
			score.append('-4 ')
			score_total += -4
		
		elif result_trace[0][y] == result_trace[1][y]:
			score.append(' 1 ')
			score_total += 1
		elif result_trace[0][y] != result_trace[1][y]:
			score.append('-8 ')
			score_total += -8
	print(result_trace)
	print(' '+ '  '.join(list(''+result_trace[0])))
	print(''.join([' | ' for x in result_trace[0]]))
	print(' '+ '  '.join(list(''+result_trace[1])))
	print(''.join(score)+ f'TOTAL: {score_total}\n\n')
	return f'\n'

print_alignment(result_trace)
print_alignment(('THEFASTCAT', 'THE----RAT'))
print_alignment(('THE-FASTCAT', 'THER-A-T---'))
print_alignment(('THE-RA-T---', 'THEF-ASTCAT'))