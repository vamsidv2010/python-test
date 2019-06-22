'''
Created on Jun 22, 2019

@author: Haritha
'''
def main():
    
    it = [1,2,4,3,5,6,78,9,-2,-98]
    n=20
    m,l,iter=iter_sample(it, n)
    
    
    # added for testing the files in the code for the git hub files and there will be less commands to the list
    
    print(m,l)
    for x in iter:
        print(x.value)
    
         
if __name__ == '__main__':main()