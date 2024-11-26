# Vinst i ett företag är 80 miljoner kr. Ställ upp en funktion som anger 
# vinsten y (i kronor) efter x år om vinsten förväntas:

# a) Öka med 15% varje år
# b) Minska med 15% varje år
y = 80*10**6
profit =1.15
loss =0.85

print(f"Nästa år blir vinsten som har en förändringsfaktor på 15, ")
print(f"{y*profit}")

print(f"Nästa år blir vinsten som har en förändringsfaktor på -15, ")
print(f"{y*loss}")