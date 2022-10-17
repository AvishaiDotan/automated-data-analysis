# Import pack's that runs the XP
import pandas as pd
import glob
from past.builtins import raw_input
import os
from Defaults import Dot_Production


# input the raw data-files path
path = raw_input("Enter your FILES path : ")
print("Input Path: " + path)


# Function to rename multiple files
def main():
    folder = path
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count+1)}.csv"
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        #os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()

# Creating a new folder Path to the data files and export combined data file



# input the raw data-files file type
file_type = ''
while file_type != 'csv' and file_type != 'xlsx':
    file_type = raw_input(r"Enter your file type (csv\xlsx): ")

    # Combine, Based on file type, the raw files to 1 file named 'combined-data-files'
    if file_type == 'csv':
           print("File type: " + file_type)
           all_files = glob.glob(path + "/*.csv")
           li = []
           for filename in all_files:
               df = pd.read_csv(filename, index_col=None, header=0)
               li.append(df)
           df = pd.concat((pd.read_csv(f) for f in all_files))

    elif file_type == 'xlsx':
           print("File type: " + file_type)
           all_files = glob.glob(path + "/*.xlsx")
           li = []
           for filename in all_files:
               df = pd.read_xlsx(filename, index_col=None, header=0)
               li.append(df)
           df = pd.concat((pd.read_xlsx(f) for f in all_files))
    else:
        print('error')


# Create a Directory path to all the files that will export '\OutPut'
directory = "Output"
# Parent Directory path
parent_dir = path
# Path
iWill_Create = os.path.join(parent_dir, directory)
# Create the directory
os.mkdir(iWill_Create)

# Creating A combined data file named 'combined-data-files'
RAW_COMBINED = path + '\Output\Raw_Combined_Data.xlsx'
# save the combined data file as xlxs
df.to_excel(RAW_COMBINED, index = False)





# clear from combined raw data file var's that we don't want based on default\specific var's
#print instruction
print("please look at the raw file var's and select the one's that u need to keep \ or select default programed system")

what_to_drop = raw_input('drop function: default\specific\ No Drop: ')
print("Drop_Function: " + what_to_drop)

# default drop list
if what_to_drop == 'default':
    # the default drop list
       drop_list = ['Opp1_Value', 'Opp2_Value', 'Opp1_pos',
                    'Opp2_pos', 'Opp1_start_time', 'Opp1_duration', 'Operator_start_time',
                    'Operator_duration', 'Opp2_start_time', 'Opp2_duration', 'Target_start',
                    'Target_duration', 'Target_pos', 'ISI_response', 'ISI_Trial',
                    'Opp1_Random_Size_Activation', 'Opp2_Random_Size_Activation',
                    'Resp_Random_Size_Active', 'Loading_Fixed.thisRepN',
                    'Loading_Fixed.thisTrialN', 'Loading_Fixed.thisN',
                    'Loading_Fixed.thisIndex', 'Loading_Variable.thisRepN',
                    'Loading_Variable.thisTrialN', 'Loading_Variable.thisN',
                    'Loading_Variable.thisIndex', 'Inst_Loop_01.thisRepN',
                    'Inst_Loop_01.thisTrialN', 'Inst_Loop_01.thisN',
                    'Inst_Loop_01.thisIndex', 'Inst_Loop_02.thisRepN',
                    'Inst_Loop_02.thisTrialN', 'Inst_Loop_02.thisN',
                    'Inst_Loop_02.thisIndex', 'Practice_Base.thisTrialN', 'Practice_Base.thisN',
                    'Practice_Base.thisIndex', 'Repeat_Base.thisN', 'Repeat_Base.thisIndex',
                    'Block_Base.thisRepN', 'Block_Base.thisTrialN', 'Block_Base.thisN',
                    'Block_Base.thisIndex', 'Inst_Loop_03.thisRepN',
                    'Inst_Loop_03.thisTrialN', 'Inst_Loop_03.thisN',
                    'Inst_Loop_03.thisIndex', 'Practice_XP.thisTrialN', 'Practice_XP.thisN', 'Practice_XP.thisIndex',
                    'Repeat_Trial.thisN', 'Repeat_Trial.thisIndex', 'Block_XP.thisRepN',
                    'Block_XP.thisTrialN', 'Block_XP.thisN', 'Block_XP.thisIndex',
                    'Inst_Loop04.thisRepN', 'Inst_Loop04.thisTrialN', 'Inst_Loop04.thisN',
                    'Inst_Loop04.thisIndex', 'key_resp.keys', 'key_resp.rt',
                    'Animation_Key.keys', 'Animation_Key.rt', 'response_key_resp.keys', 'response_key_resp.started',
                    'response_key_resp.stopped', 'diameters',
                    'Progress_Counter_Block_Base_Key.keys',
                    'Progress_Counter_Block_Base_Key.rt',
                    'Progress_Counter_Block_Base_Key.started',
                    'Progress_Counter_Block_Base_Key.stopped',
                    'Progress_Counter_Block_Base_Text.started',
                    'Progress_Counter_Block_Base_Text.stopped',
                    'Progress_Counter_Text.started', 'Progress_Counter_Text.stopped',
                    'Progress_Counter_Key.keys', 'Progress_Counter_Key.rt',
                    'dominant Hand (L\R)', 'Age', 'Gender (M\F)', 'date',
                    'psychopyVersion', 'frameRate']
       drop_list = Dot_Production.drop_list
       print("default var's will be deleted from file")

# specific drop list
elif what_to_drop == 'specific':
       listy = pd.read_excel(RAW_COMBINED).columns
       keeplist =[]
       varName = ''

       while varName != 'quit':
           varName = raw_input("Enter a var to keep \ else write 'quit': ")
           print("keep var " + varName)
           keeplist.append(varName)
       print('Keep This list as a Default: ')
       print(keeplist)

       new_list = [var for var in listy if var not in keeplist]
       print("Those var's will be deleted from file: ")
       print(new_list)
       drop_list = new_list
else:
       pass

# Clear the unwanted variabels
if what_to_drop == 'specific' or what_to_drop == 'default':
    df.drop(drop_list, inplace=True, axis=1)
else:
    print('non has been dropped')

# Save file
FIXED_RAW_COMBINED = path + '\Output\Raw_Combined_After_Dropping_unnecessary_vars.xlsx'
df.to_excel(FIXED_RAW_COMBINED, index = False)




# Split file to data based on raws \ or in lab-tangue baseline blocks and XP blocks

# Split Practice
Do_U_Want_Split = raw_input(r"Do you want to split the file (y\n?): ")
if Do_U_Want_Split == 'y':
   Split_Function = raw_input(r"Split function: default\specific: ")
   if Split_Function == 'default':

       p_df = df[(df['Practice_Base.thisRepN'] == 0) | (df['Practice_XP.thisRepN'] == 0)]
       path_df = path + '\Output\Raw_Practice_Data.xlsx'
       p_df.to_excel(path_df, index=False)

       XP_df = df[(df['Repeat_Base.thisTrialN'] == 0) | (df['Repeat_Trial.thisTrialN'] == 0)]
       # Save File
       path_df = path + '\Output\Raw_XP_Data.xlsx'
       XP_df.to_excel(path_df, index=False)

       Baseline_XP_df = df[(df['Repeat_Base.thisTrialN'] == 0)]
       # Save File
       path_df  = path + '\Output\Baseline_Data.xlsx'
       Baseline_XP_df.to_excel(path_df, index=False)

       Trial_XP_df = df[(df['Repeat_Trial.thisTrialN'] == 0)]
       # Save File
       path_df = path + '\Output\Trial_XP_Data.xlsx'
       Trial_XP_df.to_excel(path_df, index=False)

       # statistics
       File_list = [(path + '\Output\Baseline_Data.xlsx'), path + '\Output\Trial_XP_Data.xlsx']
       Part = ['Baseline', 'Trial']
       for i in Part:
           directory = i
           # Parent Directory path
           parent_dir = path + r'\Output'
           # Path
           iWill_Create = os.path.join(parent_dir, directory)
           # Create the directory
           os.mkdir(iWill_Create)

       pPart = 0
       for i in File_list:
           #Baseline_Data = path + '\Output\Baseline_Data.xlsx'
           df = pd.read_excel(i)

           # add zscore of rt and created circles based on groups
           zscore = lambda x: (x - x.mean()) / x.std()
           df.insert(10, 'Zcreated', df.groupby(['corrAns'])['Response_Num_circls'].transform(zscore))
           df.insert(11, 'Zrt', df.groupby(['corrAns'])['response_key_resp.rt'].transform(zscore))

           z_BaselineData = path + '\Output\\' + Part[pPart] + '\\z_Data.xlsx'
           df.to_excel(z_BaselineData, index=False)

           clear_z_df_prod = df[((df['Zcreated'] < -2.5) | (df['Zcreated'] > 2.5))] # | ((df['Zrt'] < -2.5) | (df['Zrt'] > 2.5)
           # fixed 27.04
           #clear_z_df_prod = clear_z_df_prod.groupby('participant').describe()
           clear_z_df_prod = clear_z_df_prod.groupby(['participant', 'corrAns'])['Response_Num_circls'].describe().ffill().reset_index()
           #clear_z_df_prod = clear_z_df_prod.iloc[:, 0:1]
           clear_z_df_prod = clear_z_df_prod.iloc[:, 0:3]
           file_path = path + '\Output\\' + Part[pPart] + '\\clear_z_df_prod.xlsx'
           clear_z_df_prod.to_excel(file_path, index=True)


           clear_z_df_rt = df[((df['Zrt'] <= -2.5) | (df['Zrt'] >= 2.5))]
           #clear_z_df_rt = clear_z_df_rt.groupby('participant').describe()
           clear_z_df_rt = clear_z_df_rt.groupby(['participant', 'corrAns'])['Response_Num_circls'].describe().ffill().reset_index()
           #clear_z_df_rt = clear_z_df_rt.iloc[:, 0:1]
           clear_z_df_rt = clear_z_df_rt.iloc[:, 0:3]
           file_path = path + '\Output\\' + Part[pPart] + '\\clear_z_df_rt.xlsx'
           clear_z_df_rt.to_excel(file_path, index=True)


           # removing:
           df = df[((df['Zcreated'] > -2.5) & (df['Zcreated'] < 2.5))] # & ((df['Zrt'] > -2.5) & (df['Zrt'] < 2.5))
           file_path = path + '\Output\\' + Part[pPart] + '\\Fixed_z.xlsx'
           df.to_excel(file_path, index=True)

           if pPart == 0:
               df['Counts'] = df.groupby(['participant'])['Response_Num_circls'].transform('count')



               df = df[(df['Counts'] > 20)]
               Fixed_BaselineData = path + '\Output\\' + Part[pPart] + '\\Fixed_Data.xlsx'
               df.to_excel(Fixed_BaselineData, index=False)
               print(df.groupby('participant').describe())
           elif pPart == 1:
               df['Counts'] = df.groupby(['participant'])['Response_Num_circls'].transform('count')



               df = df[(df['Counts'] >= 45)]
               Fixed_BaselineData = path + '\Output\\' + Part[pPart] + '\\Fixed_Data.xlsx'
               df.to_excel(Fixed_BaselineData, index=False)
               print(df.groupby('participant').describe())
           pPart += 1


   elif Split_Function == 'specific':
       output_files = []
       How_Much_Splits = raw_input(r"How much splits do u want? (n = 3, 4, 5): ")

       for i in range(int(How_Much_Splits)):
           NAMES = []
           Blocks = raw_input("For the " + str(i+1) + " Time, How much Blocks in your split? (max 4, min 1): ")
           if int(Blocks) > 4:
               Blocks = 4
               print('max 4 Blocks as default')
           if int(Blocks) < 1:
               Blocks = 1
               print('min 1 Blocks as default')

           Blocks_Name = []
           for i in range(int(Blocks)):
                block_name = raw_input("Wrote the Block var: ")
                Blocks_Name.append("" + str(block_name + ""))
                print('block name', Blocks_Name[i])

           Mark_Num = raw_input("Which number mark the varibels as Block (0 or 1): ")
           print(Mark_Num)

           print(Mark_Num)
           if Mark_Num == 0 or Mark_Num == 1:
               pass
               print(Mark_Num)
           else:
               print('error while defining Mark_Num_XP')
               Mark_Num == 0
               print(Mark_Num)

           MN = Mark_Num
           print(MN)

           if Blocks == '4':
               df = df[(df[Blocks_Name[0]] == MN) | (df[Blocks_Name[1]] == MN) | (df[Blocks_Name[2]] == MN) | ( df[Blocks_Name[3]] == MN)]
           elif Blocks == '3':
               df = df[(df[Blocks_Name[0]] == MN) | (df[Blocks_Name[1]] == MN) | (df[Blocks_Name[2]] == MN)]
           elif Blocks == '2':
               df = df[(df[Blocks_Name[0]] == MN) | (df[Blocks_Name[1]] == MN)]
           elif Blocks == '1':
               df = df[(df[Blocks_Name[0]] == MN)]
           print(df)

           # Save File
           Name_The_Block = raw_input("Name The Block(as var): ")
           Save_file_name = path + '\Output\\' + Name_The_Block +'.xlsx'
           NAMES.append(save_file_name)
           if len(NAMES) == int(Blocks):
               output_files.append(NAMES)

           df.to_excel(Save_file_name, index=False)
   else:
       print('error')
       pass




###########################################################################################

# Default vars to split as practice blocks
if Split_Practice == "default":
    practice_df = df[(df['Practice_Base.thisRepN'] == 0) | (df['Practice_XP.thisRepN'] == 0)]
    # Save File
    Practice_Data = path + '\Output\Practice_Data.xlsx'
    practice_df.to_excel(Practice_Data, index = False)



# Split XP
Split_Practice = raw_input("Split XP function: default\specific\ No Split: ")
print("Split File Function: " + Split_Practice)

# Default vars to split as practice blocks
if Split_Practice == "default":
    practice_df = df[(df['Repeat_Base.thisTrialN'] == 0) | (df['Repeat_Trial.thisTrialN'] == 0)]
    # Save File
    Practice_Data = path + '\Output\XP_Data.xlsx'
    practice_df.to_excel(Practice_Data, index=False)




if 1 == 0: # clear
    XP_df = df[(df['Repeat_Base.thisTrialN'] == 0) | (df['Repeat_Trial.thisTrialN'] == 0)]
    XP_Data = path + '\Output\XP_Data.xlsx'
    # Save the dataframe
    XP_df.to_excel(XP_Data, index = False)


#create seperate file to Baseline_XP remove rows by filtering
Split_Practice = raw_input("Split Baseline function: default\specific\ No Split: ")
print("Split File Function: " + Split_Practice)

# Default vars to split as practice blocks
if Split_Practice == "default":
    practice_df = df[(df['Repeat_Base.thisTrialN'] == 0)]
    # Save File
    Practice_Data = path + '\Output\Baseline_Data.xlsx'
    practice_df.to_excel(Practice_Data, index=False)


#create seperate file to Baseline_XP remove rows by filtering

if 1 == 0:
    Baseline_XP = df[(df['Repeat_Base.thisTrialN'] == 0)]
    Baseline_Data = path + '\Output\Baseline_Data.xlsx'

    # Save the dataframe
    Baseline_XP.to_excel(Baseline_Data, index = False)

#create seperate file to Trial_XP remove rows by filtering
Split_Practice = raw_input("Split Trial_XP function: default\specific\ No Split: ")
print("Split File Function: " + Split_Practice)

# Default vars to split as practice blocks
if Split_Practice == "default":
    practice_df = df[(df['Repeat_Trial.thisTrialN'] == 0)]
    # Save File
    Practice_Data = path + '\Output\Trial_XP_Data.xlsx'
    practice_df.to_excel(Practice_Data, index=False)


if 1 == 0: #clear
    Trial_XP = df[(df['Repeat_Trial.thisTrialN'] == 0)]
    Trial_XP_Data = path + '\Output\Trial_XP_Data.xlsx'

    # Save the dataframe
    Trial_XP.to_excel(Trial_XP_Data, index=False)
    # df = pd.read_excel('E:\Exp_Folder\סטטיסטיקה\Xp1 - A\XP1 - A_rData\Baseline_XP.xlsx')
    # CorrAns_Mean =  df.groupby('corrAns').mean()

#statistics
Baseline_Data = raw_input("Enter your Baseline_Data path : \ default")
if Baseline_Data == 'default':
    Baseline_Data = path + '\Output\Baseline_Data.xlsx'
else:
    Baseline_Data = Baseline_Data
print("Input Path: " + path)
df = pd.read_excel(Baseline_Data)


#add zscore of rt and created circles based on groups
zscore = lambda x: (x - x.mean()) / x.std()
df.insert(10, 'Zcreated', df.groupby(['corrAns'])['Response_Num_circls'].transform(zscore))
df.insert(11, 'Zrt', df.groupby(['corrAns'])['response_key_resp.rt'].transform(zscore))

z_BaselineData = path + '\Output\z_BaselineData.xlsx'
df.to_excel(z_BaselineData, index = False)



#descriptives for participants to know n of responses before clearing data that is 2.5 zscore
print(df.groupby('participant').describe())

#removing:
df = df[((df['Zcreated'] > -2.5) & (df['Zcreated'] < 2.5)) & ((df['Zrt'] > -2.5) & (df['Zrt'] < 2.5))]
print(df.groupby('participant').describe())

df['Counts'] = df.groupby(['participant'])['Response_Num_circls'].transform('count')
print(df)



df = df[(df['Counts'] > 24)]

Fixed_BaselineData = path + '\Output\Fixed_BaselineData.xlsx'
df.to_excel(Fixed_BaselineData, index = False)
print(df.groupby('participant').describe())



#######################################
df = pd.read_excel(Trial_XP_Data)


#add zscore of rt and created circles based on groups
zscore = lambda x: (x - x.mean()) / x.std()
df.insert(10, 'Zcreated', df.groupby(['corrAns'])['Response_Num_circls'].transform(zscore))
df.insert(11, 'Zrt', df.groupby(['corrAns'])['response_key_resp.rt'].transform(zscore))

z_XP_Data = path + '\Output\z_XP_Data.xlsx'
df.to_excel(z_XP_Data, index = False)

#descriptives for participants to know n of responses before clearing data that is 2.5 zscore
print(df.groupby('participant').describe())

#removing:
df = df[((df['Zcreated'] > -2.5) & (df['Zcreated'] < 2.5)) & ((df['Zrt'] > -2.5) & (df['Zrt'] < 2.5))]
print(df.groupby('participant').describe())

df['Counts'] = df.groupby(['participant'])['Response_Num_circls'].transform('count')


df = df[(df['Counts'] > 48)]

Fixed_XP_DATA = path + '\Output\Fixed_XP_DATA.xlsx'
df.to_excel(Fixed_XP_DATA, index = False)
print(df.groupby('participant').describe())


