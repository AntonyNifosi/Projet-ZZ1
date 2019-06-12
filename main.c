#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct transaction
{
    char adr[200];
    int occ;
    float value;
};

void addEntry (struct transaction tr[1000], char adr[1000], int *size, float value)
{
    int i;
    int add = 0;
    for (i = 0; i < *size; i++)
    {
        if (strcmp(tr[i].adr, adr) == 0)
        {
            tr[i].occ++;
            tr[i].value += value;
            add = 1;
        }
    }

    if (!add)
    {
        strcpy(tr[*size].adr, adr);
        tr[*size].occ++;
        tr[*size].value += value;
        (*size)++;
    }
}




int main()
{
    int i, j;
    int size = 0;
    FILE *f = fopen("logs_tx.log", "r");
    FILE *f2 = fopen("results.txt", "w");

    struct transaction tr[1000];
    char ligne[1000];
    char merde[100];
    float val;



    for (i = 0; i < 1000; i++)
    {
        tr[i].occ = 0;
        tr[i].value = 0;
    }

	for (j = 0; j < 8; j++) /* On supprime les lignes d'entetes qui ne servent a rien */
	{
	    memset(ligne, 0, 1000);
            fgets(ligne, 1000, f);
	}
	
    for (i = 0; i < 1000; i++)
    {
        for (j = 0; j < 17; j++)
        {
            memset(ligne, 0, 1000);
            fgets(ligne, 1000, f);
        }

        /* On choppe les valeurs */

        sscanf(ligne, "                 value: %f,", &val);
       

        for (j = 0; j < 8; j++)
        {
            memset(ligne, 0, 1000);
            fgets(ligne, 1000, f);
        }

        addEntry(tr, ligne, &size, val);

        for (j = 0; j < 9; j++)
        {
            memset(ligne, 0, 1000);
            fgets(ligne, 1000, f);
        }
    }



    printf("Nombre d'adresse differente : %d\n", size);

    for (i = 0; i < size; i++)
    {
        printf("Adresse : [%s] / Occurence = %d\n", tr[i].adr, tr[i].occ);
    }  


    for (i = 0; i < size; i++)
    {
        memset(merde, 0, 100);
        sprintf(merde, "%d;%f\n", tr[i].occ, tr[i].value);
        fwrite(merde, 100, 1, f2);
    }

    fclose(f);
    fclose(f2);

    return 0;
}
