#include <iostream>
#include <string>
#include <time.h>
using namespace std;
void Split(int ExerciseNum);
string mem[3] = {"PER1: ","PER2: ","PER3: "};
int memLoad[3] = {0,0,0};  // Define initials here

int main() {
    int ExerciseNum;
    cin >> ExerciseNum;
    Split(ExerciseNum);
    return 0;
}

void Split(int ExNum){
    int len = sizeof(memLoad)/ sizeof(memLoad[0]);
    int maxLoad = ExNum / len + 1;
    srand((unsigned)time(NULL)); // Preparation calcs

    for(int i=0;i<len;i++){ // Shuffle the order of member list, eliminate the error by random and logics.
        int randIndex = rand()%3;
        if(randIndex!=i){
            string temp = mem[i];
            mem[i] = mem[randIndex];
            mem[randIndex] = temp;
        }
    }
    for(int i=0;i<ExNum;i++){ // Assign works
        int chosenMem = rand()%len;
        while(memLoad[chosenMem]>=maxLoad){
            chosenMem = rand()%len;
        }
        for(int j=0;j<len;j++){
            //if(j!=chosenMem&&memLoad[j]<memLoad[chosenMem]){chosenMem=rand()%2==0?j:chosenMem;}
            if(j!=chosenMem&&memLoad[j]<memLoad[chosenMem]){chosenMem=rand()%1==0?j:chosenMem;}
        }
        memLoad[chosenMem]++;
        mem[chosenMem].append(to_string(i+1));
        mem[chosenMem].append(" ");
    }
    for(int i=0;i<len;i++){cout << mem[i] << endl;} // Disp
}