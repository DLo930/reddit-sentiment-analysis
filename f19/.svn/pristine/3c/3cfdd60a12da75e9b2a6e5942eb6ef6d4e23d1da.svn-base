from gradeC0 import *

def test_is_in():
   print "="*50
   print "Testing is_in()"
   return 1 if expect_success("is_in") else 0

def test_insert():
   print "="*50
   print "Testing insert()"
   return 1 if expect_success("insert") else 0

def test_delete():
   print "="*50
   print "Testing delete()"
   return 1 if expect_success("delete") else 0
 

def main():
   is_in_score = test_is_in()
   insert_score = test_insert()
   delete_score = test_delete()
   #remove_duplicates_score = test_remove_duplicates()

   print "="*50
   print "Task 1: "+("Complete" if is_in_score > 0 else "Incomplete")
   print "Task 2: "+("Complete" if insert_score > 0 else "Incomplete")
   print "Task 3: "+("Complete" if delete_score > 0 else "Incomplete")
   #print "Task 4: "+("Complete" if remove_duplicates_score > 0 else "Incomplete")
   
   print json.dumps({'scores': {'is_in': is_in_score,
                                'insert': insert_score,
                                'delete': delete_score}})

if __name__ == "__main__":
   print "TESTING..."
   main()
    
