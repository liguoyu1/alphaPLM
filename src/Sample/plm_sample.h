#ifndef PLM_SAMPLE_H_
#define PLM_SAMPLE_H_

#include <string>
#include <vector>
#include <string.h>

using namespace std;

const string spliter = " ";
const string innerSpliter = ":";
const string tab_spliter = "\t";

class plm_sample
{
public:
    int y;
    vector<pair<string, double> > x;
    string imei;
    plm_sample(const string& all_line);
};

vector<string> split(const string& str, const string& delim) {  
	vector<string> res;  
	if("" == str) return res;  
	//先将要切割的字符串从string类型转换为char*类型  
	char * strs = new char[str.length() + 1] ; //不要忘了  
	strcpy(strs, str.c_str());   
 
	char * d = new char[delim.length() + 1];  
	strcpy(d, delim.c_str());  
 
	char *p = strtok(strs, d);  
	while(p) {  
		string s = p; //分割得到的字符串转换为string类型  
		res.push_back(s); //存入结果数组  
		p = strtok(NULL, d);  
	}  
 
	return res;  
} 
// --------------------- 
// 作者：glmushroom 
// 来源：CSDN 
// 原文：https://blog.csdn.net/glmushroom/article/details/80690881 
// 版权声明：本文为博主原创文章，转载请附上博文链接！


plm_sample::plm_sample(const string& all_line)
{
    this->x.clear();
    this->imei.clear();
    vector<string> terms = split(all_line, tab_spliter);
    if(terms.size()<14) return ;
    this->imei = terms[1];
    string line = terms[0]+" "+terms[terms.size()-1];

    size_t posb = line.find_first_not_of(spliter, 0);
    size_t pose = line.find_first_of(spliter, posb);
    int label = atoi(line.substr(posb, pose-posb).c_str());
    this->y = label > 0 ? 1 : -1;
    string key;
    double value;
    while(pose < line.size())
    {
        posb = line.find_first_not_of(spliter, pose);
        if(posb == string::npos)
        {
            break;
        }
        pose = line.find_first_of(innerSpliter, posb);
        if(pose == string::npos)
        {
            cout << "wrong line input\n" << line << endl;
            throw "wrong line input";
        }
        key = line.substr(posb, pose-posb);
        posb = pose + 1;
        if(posb >= line.size())
        {
            cout << "wrong line input\n" << line << endl;
            throw "wrong line input";
        }
        pose = line.find_first_of(spliter, posb);
        value = stod(line.substr(posb, pose-posb));
        if(value != 0)
        {
            this->x.push_back(make_pair(key, value));
        }
    }
}


#endif /*PLM_SAMPLE_H_*/
