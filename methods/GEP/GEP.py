import random

functions = ['+','-','*','/']
termianls = ['x','y','z']
def generate_gene(head_length,tail_length):
    head = random.choices(functions,k=head_length)
    tail = random.choices(termianls,k=tail_length)
    return head+tail
# 生成随机的基因组
def generate_chromosome(gene_length,num_genes):
    return [generate_gene(gene_length//2,gene_length//2) for _ in range(num_genes)]

def express_genes(gene):
    stack = []
    for symbol in reversed(gene):
        if symbol in functions:
            if len(stack) >= 2:
                arg1 = stack.pop()
                arg2 = stack.pop()
                stack.append((symbol,[arg1,arg2]))  
            else:
                stack.append((symbol,['terminal','terminal']))
        else:
            stack.append(symbol)
    return stack[0] if stack else 0

gene_length = 10
num_genes = 2
chromosome = generate_chromosome(gene_length,num_genes)
expressed_et = [express_genes(gene) for gene in chromosome]

print("染色体:", [''.join(gene) for gene in chromosome])
print("表达的表达式树:", expressed_et)