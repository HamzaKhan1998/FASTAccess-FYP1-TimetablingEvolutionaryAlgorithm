#include<iostream>
using namespace std;
main()
{

	int m,n,noofsub,q=8	;
	int count=1,ccount=1;
	int k=0; //index of timetable
	int pcheck;
	int mcount;
	char teachercombination;
	
	cout<<"Please enter number of subjects: "<<endl;
	cin>>noofsub; //5

	string subjects[noofsub+1];
	int noofsec[noofsub];

	cout<<"Please enter the subjects : "<<endl; //oop dld pst eng cal
	for(int i=0;i<noofsub;i++)
	{
		cin>>subjects[i];
	}

	
//	cout<<"Please enter number of sections of each subject accordingly: "<<endl; //5
//	for(int i=0;i<noofsub;i++)
//	{
//		cout<<subjects[i]<<" : ";
//		cin>>noofsec[i];
//	}

	cout<<"Kindly select the option for number of teachers and their relevant combination: "<<endl;
	cout<<"a) All different for 5 sections"<<endl<<"b) A&B have same teacher, C&D have same teacher, E has a teacher"<<endl<<"c) A&B&C has same teacher and D&E has same teacher"<<endl;
	cin>>teachercombination;
	cout<<"Please assign number of rooms: "<<endl;
	cin>>m; //5
	cout<<"Please assign number of timeslots: "<<endl;
	cin>>n; //5
	string timetable[m*n];
	//cout<<"m: "<<m<<endl<<"n: "<<n<<endl;
	for(int i=0;i<n;i++)
	{
		cout<<"\t"<<i<<"\t";
	}
	cout<<endl;
	for(int i=0;i<m;i++)
	{
		//cout<<"i: "<<i<<endl;
		for(int j=0;j<n;j++)
		{
			if(subjects[j]=="\0")
			{
				cout<<"Last subject assigned!"<<endl;
				//cout<<"k: "<<k<<endl;
				mcount=n-k;
				cout<<"mcount: "<<mcount<<endl;
				for(int h=0;h<mcount;h++)
				{
					timetable[k]="empty";
					cout<<"\t"<<timetable[k]<<"\t";
					k++;
				}
				break;
				
			}
			cout<<"j: "<<j<<endl;
//			cout<<"k: "<<k<<endl;
			//cout<<"count: "<<count<<endl;
			if(teachercombination=='a')
			{
				
			}
			else if(teachercombination=='b')
			{
				//cout<<"in b"<<endl;
				//cout<<"in c"<<endl;
				//cout<<subjects[j]<<" ";
				//cout<<"o "<<endl;
				if(count==1)
				{
					//cout<<"in count 1"<<endl;
					if(ccount==1)
					{
						cout<<"301";
						ccount=0;
					}
					
					if(subjects[j]==timetable[k])
					{
						
					}
					else
					{
						//cout<<"in else 1"<<endl;
						timetable[k]=subjects[j];
						cout<<"\t"<<timetable[k]<<"\t";
						
					}
				}
				else if(count==2)
				{
					//cout<<"in count 2"<<endl;
					if(ccount==1)
					{
						cout<<endl<<"302";
						ccount=0;
					}
					for(int l=0;l<n;l++) // CHecking in a slot in above direction if a clash exits
					{
						//cout<<"l: "<<l<<endl;
						//cout<<"subjects[j] : "<<subjects[j]<<endl;
						if(subjects[j]==timetable[k-q]) //Checking elements above in increments of 5
						{
							//cout<<"in iff"<<endl;
							//cout<<"pcheck: "<<pcheck<<endl;
							if(pcheck==1) //Activated to assign the course which was left eg:OOP(b)
							{
								timetable[k]=subjects[j-1];  
								pcheck=0;
								//cout<<"in ooo"<<endl;
								cout<<"\t"<<timetable[k]<<"\t";
								break;
							}
							else
							{
								//cout<<"in ppp"<<endl;
								if(subjects[j+1]==timetable[k-k]) // Activated when to assign a next course eg: OOP(a) and DLD(b)
									{
										cout<<"in ifff"<<endl;
									}
								else
									{
										//cout<<"in else"<<endl;
										if(subjects[j+1]=="\0")
										{
											//cout<<"in new if"<<endl;
											timetable[k]="empty";
											timetable[k+1]=subjects[j];
											cout<<"\t"<<timetable[k]<<"\t"<<timetable[k+1]<<"\t"<<endl;;
											k++;
											break;
										}
										else
										{
											timetable[k]=subjects[j+1];
											pcheck=1;
											cout<<"\t"<<timetable[k]<<"\t";
											break;
										}
										
									}
							}
							
						}
						else
						{
//							cout<<"in mmm"<<endl;
//							cout<<"k+q: "<<k+q<<endl<<"k: "<<k<<"\t"<<"q: "<<q<<endl;
//							cout<<"timetable[k] : "<<timetable[k-q+2]<<"\t"<<"subject[j] : "<<subjects[j+1]<<endl;
						}
					q=q+8;	
					}
				}
				else if(count==3)
				{
					//cout<<"in count 3"<<endl;
				}
				else if(count==4)
				{
					//cout<<"in count 4"<<endl;
					if(subjects[j]==timetable[k-5])
					{
						
					}
				}
				else
				{
					//cout<<"in count 5"<<endl;
				}	
			}
			else
			{
				
			}
			k++;
			
		}
		count++;
		ccount=1;
	}
	cout<<"HAHAHAHAHHAHAHAHAHAHA"<<endl;
//	for(int i=0;i<k;i++)
//	{
//		//cout<<"k "<<k<<endl;
//		cout<<timetable[i]<<endl;
//	}
	//cout<<"HI "<<timetable[5]<<endl;
	
			
}
			
