// deitel.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
//#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <iomanip>
using std::setw;

#include <cstdlib>
using std::rand;
using std::srand;

#include <ctime>
#include "RandomNumbers.h"

//boost begin
#include <boost/date_time/gregorian/gregorian.hpp>

//#include <iostream>
#include <iterator>
#include <algorithm>
void GetYMD(long, int &, int &, int &);
//boost end
#include <windows.h>
//#include <tchar.h>
#include <stdio.h>
void findAllFiles( std::string _patch );
void dateTimeDemo();
int randomNum();
void pointersDemo();
int maks(int * arr, int n);
#include "testclass.h"
void TestClassDemo();
#include "listone.h"
void ListDemo();
#include <python.h>
void PythonDemo(int size, char *arg[]);

int _tmain(int argc, _TCHAR* argv[])
{
    //findAllFiles("c:\\");
    //dateTimeDemo();//boost
    //randomNum();
    //pointersDemo();
    //TestClassDemo();
    //auto_ptr<int> api (new int(101));
    //ListDemo();

    //char *arg[] = {"deitel", "C:\\Python27\\MyProjects\\5\\52", "counter", ""};
    char *arg[] = {"deitel", "52", "counter", ""};
    PythonDemo(4, arg);

    return 0;
}
int maks(int *arr, int n)
{
    int m = *arr++;    //int m = *arr;    //arr++;
    while(--n)
    {
        m = max(m,*arr);
        arr++;
    }
    return m;
}
void GetYMD(long kolDays, int & yy, int & mm, int & dd)
{
    yy = static_cast<int>(kolDays / 365);
    kolDays = kolDays % 365;
    mm = static_cast<int>(kolDays / 30);
    kolDays = kolDays % 30;
    dd = kolDays;
}
void findAllFiles( std::string _patch )
{
  WIN32_FIND_DATA FindData;
  std::string modifiler_address =  _patch;
  modifiler_address += "*.sys";
  HANDLE Handle = FindFirstFile( modifiler_address.c_str() , &FindData);//ищем первый файл
  //
      std::string file_name_first = FindData.cFileName;
  //
  while( FindNextFile(Handle, &FindData) )//и только теперь проходим по нужным нам файлам
  {
    std::string file_name = FindData.cFileName;
    //Чтобы не возникало  рекурсии
    if( FindData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY )
    {
      if( ! !strcmp(FindData.cFileName, "..") )
      {
        //Новый аддресс
          /*
        std::string new_patch = _patch ;
        new_patch += file_name;
        new_patch += "/"; 

        findAllFiles( list_files, new_patch );
        */
      }
    }
    else
    {
      std::string final_address = _patch; final_address += file_name;
      //list_files.push_back( zFileInfo( final_address )  );  
                          std::cout << final_address.c_str() << "\n";
    } 
    
  }
}
void dateTimeDemo()
{
    //boost begin
    using namespace boost::gregorian;
    //
    date dateBeg(2012,1,1);
    date dateEnd(2012,7,1);
    date_period datePeriod(dateBeg, dateEnd);
    date_duration dateDuration = dateEnd - dateBeg;

    date::ymd_type ymdStruct = dateBeg.year_month_day();
    int yy,mm,dd;
    yy = ymdStruct.year;
    mm = ymdStruct.month;
    dd = ymdStruct.day;
    days kolDays = datePeriod.length();

    long lKolDays = dateDuration.days();

    int mmonth = 0;
    if(dateBeg > date(2011,12,12))
    {
        GetYMD(lKolDays, yy, mm, dd);
    }
    else
    {
    }
    //boost end
}
int randomNum()
{
    try
    {
        RandomNumbers * randomNumbers = new RandomNumbers;
        for(int i = 0; i < 1; i++)
        {
            randomNumbers->GetNumbers();
        }
        randomNumbers->PrintStr();
	    delete randomNumbers;
	    return 0;
    }
    catch (exception& e)
    {
        cerr << "Error " << e.what() << '\n';
        return 1;
    }
    catch (...)
    {
        cerr << "Unknown error \n";
        return 2;
    }
    return 0;
}
void pointersDemo()
{
    const int n = 4;
    int arr[n] = {1,3,2,5};
    int arr2[n] = {3,2,1,0};
    int m = maks(arr, n);
    cerr << "\n max = ";
    cerr << m;
    int *p = arr;
    int *q = arr2;
    while(*p++ = *q++){}
}
void TestClassDemo()
{
    TestClass a = "123";
    TestClass b = "456";
    a.Print();
    b.Print();
    cout << endl;
    a = b;
    a.Print();
    cout<<endl;
}
void ListDemo()
{
    int i = 5;
    int * pi = &i;
    Node *node = new Node(pi);
}
void PythonDemo(int size, char *arg[])
{
    PyObject *pName, *pModule, *pDict, *pFunc, *pValue;

    // Инициализировать интерпретатор Python
    Py_Initialize();

// Построить объект имени
    pName = PyString_FromString(arg[1]);

    // Загрузить объект модуля
    pModule = PyImport_Import(pName);

    // pDict – заимствованная ссылка
    pDict = PyModule_GetDict(pModule);

    // pFunc – тоже заимствованная ссылка
    pFunc = PyDict_GetItemString(pDict, arg[2]);

    if (PyCallable_Check(pFunc)) 
    {
        PyObject_CallObject(pFunc, NULL);
    } else 
    {
        PyErr_Print();
    }

    // Вернуть ресурсы системе
    Py_DECREF(pModule);
    Py_DECREF(pName);

    // Завершить интерпретатор Python
    Py_Finalize();
}
