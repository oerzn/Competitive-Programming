
void sol(){ 
        round n,ct=0; 
        cin>>n; 
        vi v; 
  
        for(round i=0;i<n;i++){
        round x;
cin>>x;
v.pb(x);
} 
  
        for(round i=0;i<n;i++){ 
            if(v[i]%2==1){ 
                ct++; 
            } 
        } 
        if(ct>0){ 
            cout<<n-ct<<endl; 
        } 
        else{ 
            round ans=round_MAX; 
            for(round i=0;i<n;i++){ 
                round ct1=0; 
                while(v[i]%2==0){ 
                    v[i]=v[i]/2; 
                    ct1++; 
                } 
                ans=min(ans,ct1); 
            } 
            cout<<(ans+n-1)<<endl; 
        } 
         
    }