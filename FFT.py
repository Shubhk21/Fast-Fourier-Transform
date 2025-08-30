# SHUBHAM KAKADE
import math
import sys
import numpy as np

def DFTHorner(coefficients):

    n = len(coefficients)
    result = []

    for k in range(n):
        theta = 2 * math.pi * k / n
        omega_k_real = math.cos(theta)
        omega_k_imag = math.sin(theta)
        omega_k = complex(omega_k_real, omega_k_imag)

        poly_val = 0
        for coeff in reversed(coefficients):
            poly_val = poly_val * omega_k + coeff
        result.append(poly_val)

    return result

def GetDFTCoefficients(input_file):
    with open(input_file, 'r') as file:
        coefficients = list(map(float, file.read().strip().split()))
    return coefficients

def FormatDFTComplexNumber(c):

    realpart = f"{c.real:.3f}"
    imag_part = c.imag if abs(c.imag) > 1e-9 else 0.0
    imagpart = f"{imag_part:.3f}"

    return f"{realpart} {imagpart}"

def WriteOutputforDFT(output_file, dft_result):

    with open(output_file, 'w') as file:
        for value in dft_result:
            file.write(FormatDFTComplexNumber(value) + "\n")

def Task1DFT(input_file, output_file):

    coefficients = GetDFTCoefficients(input_file)
    final_dft_result = DFTHorner(coefficients)

    WriteOutputforDFT(output_file, final_dft_result)

def Multipadding(arr, lengt=None):
    n = len(arr)
    if lengt is None:
        lengt =1 << (n - 1).bit_length()
    padded =  np.pad(arr, (0, lengt - n), 'constant')
    return padded


def FFT(a):
    n =len(a)
    if n == 1:
        return a
    a_even =FFT(a[::2])
    a_odd =FFT(a[1::2])
    T =[np.exp( 2j * np.pi *  k / n) * a_odd[k] for k in range(n // 2)]
    return [a_even[k] + T[k] for k in range(n // 2)] + [a_even[k] - T[k] for k in range(n // 2)]



def IFFT(a):
    n = len(a)
    a_conj =np.conjugate(a)
    final_result =FFT(a_conj)
    final_result  =np.conjugate(final_result) / n
    return final_result


def Task3MultiptwolyPoly(file1, file2, output_file):

    with open(file1, 'r') as f1:
        a =np.array([float(line.strip()) for line in f1])


    with open(file2, 'r') as f2:
        b =np.array([float(line.strip()) for line in f2])


    n =max(len(a), len(b))
    n_effective =1 << (n -1).bit_length()
    a_padded= Multipadding(a,  2 * n_effective)
    b_padded =Multipadding(b, 2 *  n_effective)

    fft_polynomial_a =FFT(a_padded)
    fft_polynomial_b =FFT(b_padded)
    product =[fft_polynomial_a[i] *  fft_polynomial_b[i] for i in range(len(fft_polynomial_a))]
    product_coefficients =IFFT(product)


    with open(output_file , 'w') as f:
        for val  in product_coefficients:
            imag_part = val.imag if abs(val.imag) > 1e-9 else 0.0
            f.write(f"{val.real:.3f} {imag_part:.3f}\n")


def FFTpadding(arr):
    n =len(arr)
    next_pow_of_2 =1 << (n - 1).bit_length()
    padded_arr =np.pad(arr, (0, next_pow_of_2 - n), 'constant')
    return padded_arr


def Task2FFT(input_file, output_file):

    with open(input_file, 'r') as f:
        coefficients = np.array([float(line.strip()) for line in f])


    padded_coefficients =FFTpadding(coefficients)


    fft_result =FFT(padded_coefficients)

    with open(output_file, 'w') as f:
        for val in fft_result:
            imag_part = val.imag if abs(val.imag) > 1e-9 else 0.0
            f.write(f"{val.real:.3f} {imag_part:.3f}\n")


def Task2IFFT(input_file, output_file):

    with open(input_file, 'r') as f:
        values =[complex(*map(float, line.strip().split())) for line in f]


    padded_values =FFTpadding(values)

    ifft_result =IFFT(padded_values)

    with open(output_file, 'w') as f:
        for val in ifft_result:
            imag_part = val.imag if abs(val.imag) > 1e-9 else 0.0
            f.write(f"{val.real:.3f} {imag_part:.3f}\n")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: Project1 <Operation> <input_file.txt> <output_file.txt>")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "MultiplyPoly":
        input_file1 = sys.argv[2]
        input_file2 = sys.argv[3]
        output_file = sys.argv[4]
        Task3MultiptwolyPoly(input_file1,input_file2,output_file)


    elif operation == "DFT-Horner" or operation == "FFT" or operation == "IFFT":
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        if operation == "DFT-Horner":
            #print('DFT Called')
            Task1DFT(input_file, output_file)
        elif  operation == "FFT":
            #print('FFT Called')
            Task2FFT(input_file, output_file)
        elif  operation == "IFFT":
            #print('IFFT Called')
            Task2IFFT(input_file, output_file)

    else:
        print("Invalid operation.")
        sys.exit(1)
