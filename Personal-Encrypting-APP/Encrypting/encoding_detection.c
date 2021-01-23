#include<stdio.h>
#include<stdlib.h>



int main() {
   char *harfler  = malloc(sizeof(char)*20);
   int ascii_son = 126;
   int ascii_ilk = 32;
   int ascii_deger = 0;
   int encoding_setup0 = 0;
   printf("input:\n");
   scanf("%c",harfler);
   ascii_deger = *harfler;
   encoding_setup0 = ascii_son-ascii_deger;
   ascii_deger = encoding_setup0 + ascii_ilk;
   printf("%d-----%c\n",ascii_deger,ascii_deger );
   //printf("%c=%c\n",*harfler,ascii_deger);

   free(harfler);
   return 0;
}
