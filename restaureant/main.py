import qrcode
image= qrcode.make("http://127.0.0.1:8000/")
image.save("qr.png")


    
# arr= [i for  ]
# sum1= 33
# yes= False
# for i in range(len(arr)):
#     c= arr[i]
#     for j in range(i+1,len(arr)):
#         c+=arr[j]
#         if sum1==c:
#             yes= True
#             break
    
#     if yes:
#         print(f"found between {i} and {j}")
#         break
    

