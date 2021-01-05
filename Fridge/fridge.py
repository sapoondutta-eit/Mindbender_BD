class Refridgerator:
    def __init__(self) -> None:
        self.shelf_top = []
        self.shelf_middle = []
        self.shelf_bottom = []
        super().__init__()
    
    def put(self, item=None, size=0, shelf=None):
        ###check for item size and put it to the shelf corresponding accordingly"
        ###top shelf(0) is the small size, middle shelf(1) is the medium size shelf and the bottom shelf(2) is the biggest
        if(item == None):
            print("Please enter something that is to be refridgerated")
            return None
        
        if(size<=0):
            print("The size cannot be negative or zero")
            return None
        
        if(size>1000):
            print("This fridge is not equipped to handle such a big item. Please buy a bigger fridge.")
            return None
        
        if(shelf<0 or shelf>=3):
            print("This fridge only has 3 shelves. Buy a bigger fridge")

        if(size>0 and size <=200 and shelf==0):
            total_size_top =sum(item['size'] for item in self.shelf_top)
            s = size + total_size_top
            if(s>200):
                self.shelf_top.append({'item':item, 'size':size})
                print(f'{item} added to small top shelf.')
            else:
                print(f'Item cannot fit within this shelf. You have {200-total_size_top}/100cm of free space.')


        elif size >= 201 and size <= 450 and shelf == 1:
            total_size_middle =sum(item['size'] for item in self.shelf_middle)
            s = size + total_size_middle
            if s <= 450:
                self.shelf_middle.append({'item':item, 'size':size})
                print(f'{item} added to medium sized middle shelf.')
            else:
                print(f'Item cannot fit within this shelf. You have {450-total_size_middle}/100cm of free space.')

        elif size >= 451 and size <= 1000 and shelf == 2:
            total_size_bottom =sum(item['size'] for item in self.shelf_bottom)
            s = size + total_size_bottom
            if s <= 500:
                self.shelf_bottom.append({'item':item, 'size':size})
                print(f'{item} added to large sized shelf.')
            else:
                print(f'Item cannot fit within this shelf. You have {1000-total_size_bottom}/100cm of free space.')
        else:
            print('Item must be placed into the right size of shelf.')
            return None

        
