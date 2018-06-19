# Encodes a list of binaries to a 2B/1Q encoded list, with values -3, -1, 1 and 3
# Assiming original level positive
def encode2b1q(bin_data):
    coded_data = []
    for i in range(len(bin_data)):
        if i % 2:
            '''if bin_data[i-1] == 0 and bin_data[i] == 0:
                coded_data.append(+1)
            elif bin_data[i-1] == 0 and bin_data[i] == 1:
                coded_data.append(+3)
            elif bin_data[i-1] == 1 and bin_data[i] == 0:
                coded_data.append(-1)
            elif bin_data[i-1] == 1 and bin_data[i] == 1:
                coded_data.append(-3)
            else:
                raise Exception("Encoding Error: Data given not binary. \
%s or %s not '1' or '0'. Full data: %s" %(bin_data[i-1], bin_data[i], bin_data))'''
            # Does the same as the code above
            coded_data.append(1 + 2*bin_data[i])
            if bin_data[i-1]:
                coded_data[int(i/2)] = -coded_data[int(i/2)]

            # If previous level negative, invert the first bit
            if i >= 2 and coded_data[int(i/2)-1] < 0:
                coded_data[int(i/2)] = -coded_data[int(i/2)]
    return coded_data

# Decodes a list of 2B/1Q data to a binary list
def decode2b1q(coded_data):
    decoded_data = []
    # If x > 0 return 0, otherwise return 1
    bit0 = lambda x: x and (1, 0)[x > 0]
    bit1 = lambda x: (0, 1)[abs(x) > 1]
    invert = lambda x: (0, 1)[x == 0]
    
    for i in range(len(coded_data)):
        decoded_data.append(bit0(coded_data[i]))
        # If previous was negative, invert the first bit
        if i > 0 and coded_data[i-1] < 0:
            decoded_data[2*i] = invert(decoded_data[2*i])
        decoded_data.append(bit1(coded_data[i]))
    return decoded_data
