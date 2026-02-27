from datetime import datetime, timedelta


class LoveCalendar:
    def __init__(self, start_date_str):
        self.start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        self.today = datetime.now()

    def days_together(self):
        """计算在一起多少天"""
        return (self.today - self.start_date).days

    def next_big_day(self):
        """下一个重要纪念日"""
        days = self.days_together()
        milestones = [100, 200, 365, 520, 666, 999, 1000, 1314, 1999, 2000]

        for m in milestones:
            if m > days:
                date = self.start_date + timedelta(days=m)
                return m, (date - self.today).days, date.strftime("%Y-%m-%d")
        return None

    def love_report(self):
        """生成恋爱报告"""
        days = self.days_together()
        next_milestone = self.next_big_day()

        report = f"""
╔══════════════════════════════════════╗
║           💕 恋爱日报 💕              ║
╠══════════════════════════════════════╣
║  今天是：{self.today.strftime('%Y年%m月%d日')}              ║
║  我们在一起已经：{days:4d} 天              ║
║                                      ║
║  💌 下一个重要日子：                 ║"""

        if next_milestone:
            report += f"""
║     第 {next_milestone[0]} 天（{next_milestone[2]}）    ║
║     还有 {next_milestone[1]} 天！                 ║"""

        report += """
║                                      ║
║  情话：你是我的全局变量，贯穿我整个   ║
║        生命周期，永不释放。           ║
╚══════════════════════════════════════╝
"""
        return report


if __name__ == "__main__":
    # 使用：设置你们的开始日期
    love = LoveCalendar("2022-09-14")  
    print(love.love_report())
