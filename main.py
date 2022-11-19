from CoronaVirusAuxillary import *

def main():
    # Not varibles names are chosen from standard matrix names from linear Alg 
    V = list()
    start = 20
    wiki =  "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Canada"

    # This code no longer suppored due to wipedia update
    # Cases = get_data(wiki)[start:]

    # Saved data from March 11  2020
    cases =  [1, 4, 5, 7, 8, 9, 1, 11, 13, 14, 20, 24, 27, 30,
                34, 47, 54, 60, 67, 78, 96, 116
             ]      
    A = [[1, i ] for i in range(0, len(cases) )]
    y = [float(ln(cases[i])) for i in range(0, len(cases)) ]

    C  = linear_regression(A, y)
    c1, c2 = C[0], C[1]

    print("Predicition in 10 days: " , int(exp(c1  + c2 *( len(y) + 10)) ), "\n")
    print("Current confirmed cases: ",  cases[-1], '\n')
    predictionPlot(A, y, cases, c1, c2)


if __name__ == '__main__':
    main()
