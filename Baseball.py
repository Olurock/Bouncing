class solution():
    ops = [1,2,'c','d','+']
    def calpoint(self,ops)->int:
        score = None
        steps =[]
        print(steps.pop())
        for i in (ops):
            if i =='c' :
                steps.pop()
            elif i=='D':
                score = steps[-1]*2
                steps.append(score)
            elif ops[i]=='+':
                score = steps[-1] + steps[-2]
                steps.append(score)
            else :
                score = int (i)
                steps.append(score)
        return score

    if __name__ == '_Baseball_':
        line = input('')
        ops = line.strip().split()
        print(ops)
        print(calpoint(ops))
