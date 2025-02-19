```csharp


namespace HelloWorld1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World, from Pratyush");
            

            int number ;
            int Number = 1;

            const float Pi = 3.14f ;
            float number2 = 3.14f;

            char c = 'A'; //single ' for char, " for 
            string s = "ABCDEF";

            bool isWorking = false;
            //cw is short for console.writeline
            Console.WriteLine(s);
            Console.WriteLine(number2);
            Console.WriteLine(Pi);

            //var for variables
            var n3 = 3; //compiler automatically detects datatype for var

            //ctrl click over var  - opens object browser
            //ctrl x deletes line

            //format string
            Console.WriteLine("Byte values {0} - {1}",byte.MinValue,byte.MaxValue);
            Console.WriteLine("FLoat vals {0} - {1} ",float.MinValue, float.MaxValue);

            const float pi2 = 3.14f;
            //cannot be changed - be careful
            ////////////////////////////////////////////////////////////////////////////////////

            //TYPE CONVERSION

            //Implicit type conversion
            byte b = 1;
            int i = b; //type conversion from lower to higher : byte -> 4 bytes 
                       // opposite wont happen - > wont compile -  bcuz data loss

            //Explicit type conversion
            int i2 = 1;
            byte b2 = (byte)i2; // this is called casting - means - we know data loss will happen
                                // we will let it happen anyway
            int i5 = 1000;
            byte b5 = (byte)i5;
            Console.WriteLine(b5);//100->232 - loss of data

            //not compatibtile -  cannot do : string s = "l";     int i = (int) s; > not posssible
            string s3 = "1";
            int i4 = Convert.ToInt32(s3);
            int j = int.Parse(s3);
            Console.WriteLine(i4);

            // ToByte() ;  ToInt16(); ToInt32() ; ToInt64()


            // TRY CATCH BLOCK  - try tab for code snippet
            Console.WriteLine("Try catch block ");
            try
            {
                var numberTry = "12345";
                byte bTry = Convert.ToByte(numberTry);
                Console.WriteLine(bTry);
            }
            catch (Exception)
            {
                Console.WriteLine("Number couldn't be converted to a byte");
            }


            Console.WriteLine("Try catch block 2 ");
            try
            {
                string sTry = "true";
                bool bTry = Convert.ToBoolean(sTry);
                Console.WriteLine(bTry);
            }
            catch (Exception)
            {
                Console.WriteLine("Number couldn't be converted to a boolean");
            }


            //OPERATORS

            //POST FIX - forst a is assigned to b then incremented by 1
            int a1 = 1;
            int b1 = a1++;
            Console.WriteLine("{0} {1}", a1, b1);// a 2 , b 1

            //PREFIX -  a is incremented by one , then assigned to b
            int a3 = 1;
            int b3 = ++a3;
            Console.WriteLine("{0} {1}", a3, b3);

            //LOGICAL OPERATORS && and || and !
            // BITWISE OPERATORS & and | 


        }
    }
}
```
