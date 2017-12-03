class LevelDict(dict):
    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if item in key:
                    return self[key]
        else:
            return super().__getitem__(item)

level_check = LevelDict({range(0, 30):  'freshman', 
                     range(30,60):  'sophomore',
                     range(60,90):  'junior',
                     range(90,999): 'senior' 
                    })
while True:
  creditstr = input('\nEnter credit level (return to end): ')
  if creditstr:
    level = level_check[int(creditstr)]
    print("Level achieved: {}".format(level))
  else:
    break