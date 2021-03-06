def get_travel_advice(temperature):
    if temperature >= 40:
        return "建议停止户外作业，对老弱病幼人士采取保护措施。"
    elif temperature >= 37:
        return "避免在高温时段进行户外活动，老弱病幼落实防暑降温保护措施。"
    elif temperature >= 35:
        return "天气闷热，适宜着丝麻、轻棉织物制作的短衣、短裙、薄短裙、短裤等夏季服装。"
    elif temperature >= 34:
        return "午后尽量减少户外活动，高温条件下作业和露天作业人员采取必要防护措施。"
    elif temperature >= 33:
        return "天气炎热，适宜着短衫、短裙、短裤、薄型T恤衫、敞领短袖棉衫等夏季服装。"
    elif temperature >= 28:
        return "天气较热，适宜着棉麻面料的衬衫、薄长裙、薄T恤等夏季服装。年老体弱者：长袖衬衫和单裤。"
    elif temperature >= 25:
        return "天气偏热，适宜着短衫、短裙、短套装、T恤等夏季服装。年老体弱者：单层薄衫裤、薄型棉衫。"
    elif temperature >= 23:
        return "天气暖和，适宜着单层棉麻面料的短套装、T恤衫、薄牛仔衫裤、休闲服、职业套装等春秋过渡装。"
    elif temperature >= 22:
        return "天气暖和，年老体弱者请适当增减衣服。"
    elif temperature >= 21:
        return "天气温暖，适宜着长袖衬衫加单裤、单层薄衫裤、薄型棉衫等春秋过渡装。"
    elif temperature >=20:
        return "天气温暖，年老体弱者推荐针织长袖衬衫＋背心、长裤、薄型套装。"
    elif temperature >= 18:
        return "天气温和，适宜着 单层薄衫裤、薄型棉衫、长裤、针织长袖衫、长袖T恤、薄型套装、牛仔衫裤、西服套装等春秋过渡装。"
    elif temperature >=16:
        return "天气温和，年老体弱者宜着针织长袖衬衫 + 马甲、长裤、夹克衫、西服套装等。"
    elif temperature >= 15:
        return "天气温凉，适宜着夹衣、马甲衬衫、长裤、夹克衫、西服套装加薄羊毛衫等春秋服装。"
    elif temperature >= 14:
        return "天气温凉，年老体弱者适宜着夹衣或风衣加羊毛衫。"
    elif temperature >= 13:
        return "天气微凉，适宜着一件羊毛衫、夹克衫、西服套装、马甲衬衫＋夹克衫配长裤等春秋着装；年老体弱者：厚外套加毛衣、呢外套加羊毛衫。"
    elif temperature >= 11:
        return "天气较凉，适宜着厚外套加毛衣、大衣、毛套装、西服套装等春秋服装。体弱者宜着大衣、毛衣加呢外套等厚型春秋服装。"
    elif temperature >= 8:
        return "天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装。"
    elif temperature >= 6:
        return "天气凉，年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。"
    elif temperature >= 5:
        return "天气微冷，适宜着毛衣、风衣、大衣、皮夹克、外套、毛套装、西装、防寒服等厚型 春秋着装。"
    elif temperature >=3:
        return "天气微冷，老年体弱者，冬季着装：一到两件羊毛衫＋大衣或毛套装、薄棉外套等"
    elif temperature >= 0:
        return "天气微冷，适宜着毛衣、风衣、大衣、皮夹克、外套、毛套装、西装、防寒服等厚型春秋着装。"
    elif temperature >= -2:
        return "天气冷，老年体弱者，冬季着装：一到两件羊毛衫＋大衣或毛套装、薄棉外套等。"
    elif temperature >= -5:
        return "天气冷，冬季着装：棉衣、羽绒衣、冬大衣、皮夹克、毛衣再外罩大衣等；年老体弱者尤其要注意保暖防冻。"
    elif temperature >= -10:
        return "天气寒冷，冬季着装：棉衣、羽绒服、冬大衣、皮夹克加羊毛衫、厚呢外套、呢帽、手套等。"
    elif temperature >=-15:
        return "天气非常寒冷，年老体弱者尽量少外出。"
    else:
        return "温度极低，尽量少外出；建议着厚棉衣、厚羽绒服、冬大衣、皮夹克、裘皮大衣、棉帽、棉手套、棉靴等隆冬着装。"
