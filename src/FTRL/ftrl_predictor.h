#ifndef FTRL_PREDICTOR_H_
#define FTRL_PREDICTOR_H_

#include "../Frame/pc_frame.h"
#include "ftrl_model.h"
#include "../Sample/plm_sample.h"


class ftrl_predictor : public pc_task
{
public:
    ftrl_predictor(bool haveNews,double _factor_num, ifstream& _fModel, ofstream& _fPredict);
    virtual void run_task(vector<string>& dataBuffer);
private:
    ftrl_model* pModel;
    ofstream& fPredict;
    mutex outMtx;
    bool have_news;
};


ftrl_predictor::ftrl_predictor(bool haveNews, double _factor_num, ifstream& _fModel, ofstream& _fPredict):fPredict(_fPredict)
{
    pModel = new ftrl_model(_factor_num);
    if(!pModel->loadModel(_fModel))
    {
        cout << "load model error!" << endl;
        exit(-1);
    }
//    else{
//        pModel->debugPrintModel();
//    }
    have_news = haveNews;
}

void ftrl_predictor::run_task(vector<string>& dataBuffer)
{
    vector<string> outputVec(dataBuffer.size());
    for(int i = 0; i < dataBuffer.size(); ++i)
    {
        plm_sample sample(dataBuffer[i], false, have_news);
        cout<<"feature size:"<<sample.x.size()<<endl;
        double score = pModel->getScore(sample.x, *(pModel->muBias), pModel->muMap);
        if(have_news)
            outputVec[i] = sample.imei+"#"+to_string(score);
        else
            outputVec[i] = to_string((sample.y+1)/2) + " " + to_string(score);//+" "+sample.imei;
    }
    outMtx.lock();
    for(int i = 0; i < outputVec.size(); ++i)
    {
        fPredict << outputVec[i] << endl;
    }
    outMtx.unlock();
}


#endif /*FTRL_PREDICTOR_H_*/
