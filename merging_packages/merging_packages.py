def get_indices_of_item_wights(arr, limit):
  need = dict()
  
  for idx, item in enumerate(arr):
    if item in need:
      return [idx, need[item]]
    else:
      need[limit - item] = idx
      
  return []
   

print(get_indices_of_item_wights([4, 6, 10, 15, 16], 20))
