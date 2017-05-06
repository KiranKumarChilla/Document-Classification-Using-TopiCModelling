
%openingfile and reading Document term matrix from file
fileId=fopen('dtmatrix.txt','r');
line = fgets(fileId);
Words = strsplit(line);
len=length(Words);
Words=Words(1:len-1);
%DocumenttermMatrix
Dtm(1,:) = Words;
wordcount=zeros(50,len-1);
for i=1:50
line = fgets(fileId);
temp = strsplit(line);
temp=temp(1:len-1);
Dtm(i+1,:)=temp;
 for j=1:len-1
     wordcount(i,j)=str2num(cell2mat(temp(j)));
end
end


%applying SVD
[U,S,V] = svd(wordcount);

Unew=U(:, 1);
Snew=S(1,1);
Vnew=transpose(V(1,:));





t=Unew*Snew;
D=Snew*Vnew;
M=zeros(50,1);
I=zeros(50,1);



%finding top words
[temp,originalpos] = sort(D(:), 'descend' );
n = temp(1:2);
p=originalpos(1:2);
fprintf('the top words are');
disp(Words(p));


%finding most interesting documents
[temp,originalpos] = sort( t(:), 'descend' );
n1 = temp(1:3);
p1=originalpos(1:3);
fprintf('the interesting documents can be');
disp(p1);


