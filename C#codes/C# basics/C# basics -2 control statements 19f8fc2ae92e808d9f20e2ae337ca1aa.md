# C# basics -2 : control statements

- Create console app

# In program.cs

```csharp
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

NewClass newClass= new NewClass();
newClass.Greet();

```

in Newclass.cs

```csharp
using System;

public class NewClass{
    public void Greet(){
        Console.WriteLine("hello checking seconf code");

        // checking condition

        bool b1 = (20>10)?  true: false;
        System.Console.WriteLine(b1);

        string s1 = (20>10)? "20 is greater than 10": "20 is less than 10";
        System.Console.WriteLine(s1);

        System.Console.WriteLine("Switch case example");

        int day = 4;

        switch (day){
            case 1: System.Console.WriteLine(0); break;
            case 2: System.Console.WriteLine(1); break;
            case 3: System.Console.WriteLine(2); break;
            case 4: System.Console.WriteLine(3); break;
            default: System.Console.WriteLine("default");   break;
        }

        System.Console.WriteLine("while loop exmpale");
        int a = 0;
        while (a < 10){
            int j = a;
            System.Console.WriteLine($"{j} {j+1} {j+2}");
            a++;
        }    

        System.Console.WriteLine("Trying bubble sort");
        int[] l = {2,1,3,4,1,2,7,4,15};

        System.Console.WriteLine("Before sorting");
        for (int i = 0; i< l.Length; i++) System.Console.WriteLine($"{l[i]} ");

        for (int i = 0; i< l.Length -1; i++){
            for(int j = 0; j< i; j++ ){
                if (l[j] > l[j+1]){
                    int check = l[j];
                    l[j] = l[j+1];
                    l[j+1] = check;
                }
            }
        }
        System.Console.WriteLine("After sorting");
        for (int i = 0; i< l.Length; i++) System.Console.WriteLine($"{l[i]} ");

        System.Console.WriteLine("array.sort and ");
        int[] l2 = {3,1,3,4,1,1,2,7,4};
        Array.Sort(l2);
        foreach (int i in l2) System.Console.Write(i);
    }
}
```

# to run

```
D:\C#-leraning\c#vsc>cd LearningCsFromConsoleApp

D:\C#-leraning\c#vsc\LearningCsFromConsoleApp>dotnet run
```