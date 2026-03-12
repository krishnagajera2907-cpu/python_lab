#include<stdio.h>
#include<conio.h>
 typedef struct xyz node;
   struct xyz
   {
     int data;
     node * next;
    };
    node* temp;
    node* first=NULL;
    node* last;
    node* ins;
    node*erase;
    int count=0;
    void add()
    {
    temp=(node*)malloc(sizeof (node));
    printf("\n\n\ enter value:");
    scanf("%d",&temp->data);
    temp->next=NULL;
    if(first==NULL)
    {
    first=temp;
    }
    else
    {
    last=temp;
    count++;
    printf("\n\n\t value inserted successfully..");
    }
}
void disp()
{
    if(first==NULL)
    {
    printf("\n\t record not found");
    }
    else
    {
	int sr=1;
	temp=first;
	while(temp!=NULL)
    {
	 printf("\n\t %d):%d",sr++,temp->data);
	 temp=temp->next;
    }
  }
}
    void srch()
    {
     if (first==NULL)
     {
     printf("\n\t record not found");
     }
     else
    {
     int sr,sv,flag=0;
     sr=1;
     temp=first;
     printf("\n\t enter search value:");
     scanf("%d",&sv);
     while(temp!=NULL)
     {
     printf("\n\t%d);%d",sr++,temp->data);
     if (temp->data==sv)
     {
     printf("<===value found here");
     flag=1;
     }
     temp=temp->next;
     }
     }
     }
      void updt()
    {
     if (first==NULL)
     {
     printf("\n\t record not found");
     }
     else
     {
     int uv,flag=0;
     disp();
     temp=first;
     printf("\n\t enter value for update:");
     scanf("%d",&uv);
     while(temp!=NULL)
     {

     if (temp->data==uv)
     {
     printf("\n\t enter new value:");
     scanf("%D",&temp->data);
     flag=1;
     }
     temp=temp->next;
     }
       if(flag==0)
       printf("\n\t value%d not found",uv);
       else
       printf("\n\t value updated__");
     }
     }

     void del()
     {
      if(first==NULL)
      {
      printf("\n\t record not found");
      }
      else
      {
      int dv,flag=0;
     printf("\n\t enter value for delete:");
     scanf("%d",&dv);
     if(first->data==dv)
     {
      erase=first;
      first=first->next;
      flag=1;
      }
      else
     {
     temp=first;
     while(temp!=NULL)
     {
       if(temp->next->data==dv)
      {
      erase=temp->next;
      if(erase==last)
      {
      last=temp;
      }
      temp->next=erase->next;
      flag=1;
      }
      temp=temp->next;
      }
      }
      if(flag==0)
      {
      printf("\n\t value%d not found",dv);
     }
     else
    {
     free(erase);
     printf("\n\t value deleted..");
     count--;
     }
     }
  }



void main()
{
 int ch;
 while(1)
 {
 clrscr();
 printf("1)add data");
 printf("\n2)display data");
 printf("\n3)remove data");
 printf("\n4)exit");
 printf("\n\n enter your choice");
 scanf("%d",&ch);
 switch(ch)
 {
  case 1:
   add();
   break;
  case 2:
   disp();
   break;
  case 3:
    del();
    break;
  case 4:
   srch();
   break;
   case 5:
    exit();
  }
   getch();
   }
   }





