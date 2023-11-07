import numpy as np
import imageio
import time



def toBinary(a):
    """
    Convert string to string of 0s and 1s
    Converts each character to its binary representation
    Zero-padded left to 8 bits
    @params
    a (string) the string to convert
    @return
    m (string) the converted string
    """
    m= ""
    for i in a:
        m+= f'{ord(i):08b}'
    return m



def EncryptImage(imageToEncrypt, message, Step = 2, startx = 0,starty = 0):
    """
    Function to hide message in imageToEncrypt
    @params
    imageToEncrypt (string) The direction to the image to use
    message (string) The message to hide
    Step (int) Distance between pixels
    startx (int) starting x coordinate
    starty (int) starting y coordinate
    """

    #Convert message from text to binary
    binnaryMssg = toBinary(message)

    #Get Image as a 3D array
    dataToEncrypt =imageio.imread(imageToEncrypt, pilmode ="RGBA")


    originalRows, originalColumns,_ = dataToEncrypt.shape


    #Define starting position
    x,y = startx,starty


    for char in binnaryMssg:
        #Make sure we are still inside the boundaries
        #of the image
        if x >= originalColumns:
            x = startx
            y += Step
            if y >= originalRows:
                    x = startx + 1
                    y = starty + 1

        #reduce the alpha chanel by 2
        dataToEncrypt[y,x,-1] = dataToEncrypt[y,x,-1] - 2*int(char)
        x += Step

    #create a new image
    imageio.imwrite("test.png",dataToEncrypt)




def DecryptImage(imageToEncrypt,Step,startx,starty):
    """
    Function to find the message in imageToEncrypt
    @params
    imageToEncrypt (string) The direction to the image to use
    Step (int) Distance between pixels
    startx (int) starting x coordinate
    starty (int) starting y coordinate
    @return
    plainText (string) the message
    """

    #Get the image as an array
    dataToDecrypt =imageio.imread(imageToEncrypt)

    originalRows, originalColumns,_ = dataToDecrypt.shape


    #We go over the image, adding 0s and 1s to the
    #binaryText string
    binaryText = ""
    for y in range(starty,originalRows,Step):
        for x in range(startx, originalColumns, Step):
            binaryText += str(int((255 - dataToDecrypt[y,x,-1])/2))

    #We separate the binaryText string into 8 bit chunks
    #(size used during encription)
    #and convert each chunk to ASCII
    plainText = ""
    for index in range(0,len(binaryText),8):
        a = int(binaryText[index:index+8],2)
        plainText += chr(a)



    return plainText




MSG = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce eu eros in felis bibendum tincidunt quis auctor lacus. Donec efficitur tristique orci. Suspendisse potenti. Cras a odio lorem. Mauris ligula metus, vulputate sed mauris at, pulvinar sagittis magna. Mauris accumsan ante ipsum, nec tempus mi cursus porta. Nullam scelerisque mauris vitae nibh consequat auctor. Donec ac dignissim ante.

Cras auctor, lorem at aliquam dapibus, nulla ligula tincidunt dui, sed porttitor neque augue eu nunc. Duis dui dolor, molestie vel eros ut, elementum vehicula metus. Morbi non enim quis tellus eleifend tempor. Phasellus iaculis nulla a tincidunt iaculis. Morbi tempus, quam a viverra vehicula, odio turpis eleifend lacus, eu ornare felis ligula vitae nisl. Praesent et mauris ligula. Duis id lacus scelerisque, consequat metus vel, volutpat nulla. Nullam cursus turpis et libero vehicula sodales.

Vestibulum in sem elit. Phasellus condimentum accumsan blandit. Nulla facilisi. Maecenas sed venenatis elit. Aenean convallis non lacus vel suscipit. Mauris ut lorem ut erat tempor elementum. Curabitur in neque non leo dapibus lobortis eget at diam. Suspendisse et molestie elit. Nam ornare at dolor vel tincidunt. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec aliquam efficitur purus, eget pellentesque odio malesuada nec. Integer elementum aliquet quam non malesuada. Nullam eget rhoncus orci. Morbi turpis nunc, aliquam vel velit ac, pretium aliquet ante. Integer tempor lectus quis risus luctus elementum.

Nam id augue et nulla porta tincidunt. Quisque cursus, augue sit amet pulvinar blandit, urna enim sodales ante, eget vehicula massa justo pharetra dolor. Fusce a ultrices quam. Proin eget urna eget sapien pellentesque blandit. Integer ut mattis nulla. Proin ultrices ligula sit amet est scelerisque, condimentum ullamcorper diam feugiat. Morbi a scelerisque augue. Donec tincidunt maximus dapibus. Sed maximus nisi ex, eget scelerisque nibh dictum ultricies. Donec mi nunc, mattis in tincidunt in, volutpat sit amet eros. Vestibulum pharetra a libero at congue. Quisque et libero non ante gravida mattis. Sed at turpis nec elit scelerisque mattis vel nec leo.

Donec odio sapien, tempor placerat ex quis, accumsan euismod lacus. Sed lobortis nisi ac tellus tincidunt lobortis. Sed vitae egestas massa. Morbi ac neque quis nibh vulputate sollicitudin. Vestibulum pellentesque metus et gravida ullamcorper. Phasellus eget sapien condimentum, finibus dui eget, sagittis mauris. Fusce pharetra sagittis urna, in gravida lorem accumsan eu. Praesent hendrerit eu ante sit amet malesuada.
"""
start = time.time()
EncryptImage("0.png",MSG);
print(f"elapsed: {time.time() - start}")

start = time.time()
print(DecryptImage("test.png",2,0,0))
print(f"elapsed: {time.time() - start}")






