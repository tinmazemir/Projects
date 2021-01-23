#include<stdio.h>
#include<stdlib.h>

#define MemCapacity  10000
#define ascii_last  127
#define ascii_first  32

void take_data();
void record_data();
void encoding_decoding_data();



FILE *filedosya;
FILE *filePointer;
char *memory;
int counterMemory;


int  main()
{
   memory = malloc(sizeof(char)*MemCapacity);
   take_data();
   encoding_decoding_data();
   record_data();
   free(memory);
   return 0;
}

void take_data()
{
   filedosya = fopen("sifrelenecek.txt","r");
   char character;
   do
   {
      character = getc(filedosya);
      printf("%c ---- ",character);
      *memory = character;
      memory++;
      printf("memory :: %c\n",*memory);
      counterMemory++;
      printf("Cmemory :: %d\n",counterMemory);

   }while(character != EOF);
   fclose(filedosya);
   remove("sifrelenecek.txt");
}


void record_data()
{
   filePointer = fopen("sifrelenmis.txt","w");
   printf("------------------\n");
   if (!filePointer)
   {
     printf("----ERROR----\n");
     exit(1);
   }
   memory = memory - counterMemory;
   for (int i = 0 ; i < counterMemory-1; i++)
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
      printf("befor encoding :%c/%d ----- ",*memory,*memory);
      *memory = (ascii_last - *memory) + ascii_first;
      printf("after encoding :%c/%d\n",*memory,*memory);
      memory++;
   }

}
