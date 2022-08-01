def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    ����һ��ֻ�����������ķǿ����顣�Ƿ���Խ��������ָ�������Ӽ���ʹ�������Ӽ���Ԫ�غ���ȡ�
    ʾ��: ����: [1, 5, 11, 5] ���: true ����: ������Էָ�� [1, 5, 5] �� [11].
    ��������ñ����㷨�����������
    �����Ӽ���Ԫ�غ���� = ��ԭ��������������Ԫ�أ�ʹ���ǵĺ�Ϊsum/2
    ���������⡿
    ԭ�����еĸ��������Կ�����ͬ����Ʒ��ÿ����Ʒ��value��weight����nums�е���ֵ
    ��ԭ�����������������뱳�����������������Ϊsum/2(�������ļ������ĺͲ�����sum/2)��ʹ�����ڵ���Ʒ��ֵ��(�������ļ������ĺ�)���
    �������ڵ���Ʒ��ֵ��Ϊsum/2,��ԭ������Է�Ϊ�����Ӽ��������Ӽ���Ԫ�غ����
    """
    if sum(nums) % 2 == 1:
        return False
    # initialization
    bagsize = int(sum(nums) / 2)
    dp = [[0] * (bagsize + 1) for _ in nums]
    for j in range(bagsize + 1):
        if j >= nums[0]:
            dp[0][j] = nums[0]
        else:
            dp[0][j] = 0
    # recursion
    for i in range(len(nums)):
        for j in range(1, bagsize + 1):
            if j < nums[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                tmp_value = dp[i - 1][j - nums[i]] + nums[i]
                dp[i][j] = max(dp[i - 1][j], tmp_value)
    return dp[-1][-1] == bagsize

nums = [1,5,11,5, 6, 8, 9, 5]
print(canPartition(nums))

