#include<stdio.h>
#include<stdlib.h>

#define MemCapacity  250
#define ascii_last  127
#define ascii_first  32

void take_data();
void record_data();
void encoding_decoding_data();



FILE *filePointer;
char *memory;
int memTemp;
int counterMemory;


int  main()
{
   printf("Input:      'press to escape button --esc-- for completing'\n");
   memory = malloc(sizeof(char)*MemCapacity);
   memTemp = memory;
   take_data();
   encoding_decoding_data();
   record_data();
   free(memory);
   printf("Completed\n");
   system("pause");
   return 0;
}


void take_data()
{
  while (1)
  {
     char character;
     character = getche();
     if (character == 27 || counterMemory == MemCapacity)
     {
       system("CLS");
       break;
     }
     else if (character == 8)
     {
       memory--;
       counterMemory--;
     }
     else if((character != 8 && character != 27) &&
            (character > ascii_first-1 && character < ascii_last+1 ))
     {
        *memory = character;
        memory++;
        counterMemory++;
     }
     else if( character < ascii_first || character > ascii_last )
     {
        printf("Error you cant use this character %c\n",character);
     }

}
}


void record_data()
{
   filePointer = fopen("sifreli.txt","a+");
   printf("------------------\n");
   if (!filePointer)
   {
     printf("----ERROR----\n");
     exit(1);
   }
   memory = memory - counterMemory;
   for (int i = 0 ; i < counterMemory; i++)
   {
     fprintf(filePointer,"%c",*memory);
     memory++;
   }

}


void encoding_decoding_data()
{
   memory = memory - counterMemory;
   for(int i = 0; i < counterMemory; i++)
   {
      //printf("befor encoding :%c/%d ----- ",*memory,*memory);
      *memory = (ascii_last - *memory) + ascii_first;
      //printf("after encoding :%c/%d\n",*memory,*memory);
      memory++;
   }

}
