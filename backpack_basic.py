'''
��01������
######## ԭ�ļ����� https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md
��n����Ʒ��һ������ܱ�����Ϊw�ı�������i����Ʒ��������weight[i]���õ��ļ�ֵ��value[i]��
***ÿ����Ʒֻ����һ�Σ���⽫��Щ��Ʒװ�뱳������Ʒ��ֵ�ܺ����
�����������Ϊ4��
��ƷΪ    weight value
     0     1      15
     1     3      20
     2     4      30
�ʱ����ܱ�����Ʒ����ֵ�Ƕ��٣�

ͬ���ö�̬�滮��������������͡�
1 ������dp���顿
ʹ�ö�ά���飬��dp[i][j] ��ʾ���±�Ϊ��0��i����Ʒ������ȡ���Ž�����Ϊj�ı�������ֵ�ܺ�����Ƕ���
2 ��dp��ʼ����
�����������jΪ0�Ļ���������ѡȡ��Щ��Ʒ��������ֵ�ܺ�һ��Ϊ0����dp����ĵ�һ�У�dp[i][0]ȫ��Ϊ0��
����dp�ĵ�һ�У���Ҫ�������в�ͬ�ı������������
�� ����Ʒ0���������ڵ�ǰ�����������jʱ��dp[0][j] = 0
�� ����Ʒ0������С�ڵ�ǰ�����������jʱ����ʾ����װ����Ʒ0��dp[0][j] = value[0]
3 �����ƹ�ʽ��
'''


