import pandas as pd

def looking_forward_percentage(df):
    total_forward_count = df["Forward"].sum()

    percentage_forward = round((total_forward_count / len(df)) * 100, 1)

    return percentage_forward

def get_blink_count(df):
    total_blink_count = df["Total Blink Count"].iloc[-1]

    total_time = df["Timestamp (ms)"].iloc[-1] - df["Timestamp (ms)"].iloc[0] # in milliseconds
    total_time_seconds = total_time / 1000

    # Calculate the average blink rate
    average_blink_rate = total_blink_count / total_time_seconds

    if average_blink_rate > (20/60): # 20 blinks per minute
        return "High Blink Rate"
    elif average_blink_rate < (10/60): # 10 blinks per minute
        return "Low Blink Rate"
    else:
        return "Normal Blink Rate"
    
def results(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return get_blink_count(df), looking_forward_percentage(df)

# if __name__ == "__main__":
#     print(results('logs\\eye_tracking_log_26-01-2025_01-42-23.csv'))