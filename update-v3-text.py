import glob, re, os, fileinput, time, sys, math
from ast import literal_eval

def deleteOldFiles():
    filePaths = [
        ".\database\\migrations\\2014_10_12_000000_create_users_table.php",
        ".\database\\migrations\\2014_10_12_100000_create_password_resets_table.php",
        ".\database\migrations\\2019_02_27_075638_create_game_tables.php",
        ".\database\migrations\\2019_04_07_130129_add_site_settings.php",
        ".\database\migrations\\2019_04_09_090831_create_user_log_table.php",
        ".\database\migrations\\2019_04_09_095513_create_currency_tables.php",
        ".\database\migrations\\2019_04_12_123405_fix_data_descriptions.php",
        ".\database\migrations\\2019_04_13_094613_add_owned_currencies.php",
        ".\database\migrations\\\2019_04_14_121447_add_transfer_flag_to_items.php",
        ".\database\migrations\\2019_04_15_122508_add_prompts_table.php",
        ".\database\migrations\\2019_04_16_062617_add_parsed_text_to_site_pages.php",
        ".\database\migrations\\2019_04_16_080112_add_invitation_keys.php",
        ".\database\migrations\\2019_04_19_125212_fix_inventory_tables.php",
        ".\database\migrations\\2019_04_20_140827_fix_user_item_log.php",
        ".\database\migrations\\2019_04_29_080228_fix_inventory_tables_again.php",
        ".\database\migrations\\2019_04_30_070721_add_notification_data.php",
        ".\database\migrations\\2019_05_04_091240_add_news.php",
        ".\database\migrations\\2019_05_11_045038_update_character_tables.php",
        ".\database\migrations\\2019_05_12_064538_add_species_id_to_images.php",
        ".\database\migrations\\2019_05_12_100722_make_features_nonunique.php",
        ".\database\migrations\\2019_05_19_054413_make_character_image_id_nullable.php",
        ".\database\migrations\\2019_05_20_075936_add_character_sort.php",
        ".\database\migrations\\2019_06_01_121701_add_changed_data_to_character_log.php",
        ".\database\migrations\\2019_06_10_083954_create_character_transfer_tables.php",
        ".\database\migrations\\2019_07_09_063021_create_raffles.php",
        ".\database\migrations\\2019_07_13_095608_create_loot_tables.php",
        ".\database\migrations\\2019_07_13_101743_create_prompt_categories.php",
        ".\database\migrations\\2019_07_15_090200_add_prompt_rewards.php",
        ".\database\migrations\\2019_07_21_161720_add_prompt_submissions.php",
        ".\database\migrations\\2019_08_06_092958_add_submission_count_to_user_settings.php",
        ".\database\migrations\\2019_08_09_123451_make_submission_prompt_id_nullable.php",
        ".\database\migrations\\2019_08_10_120818_add_myo_slots.php",
        ".\database\migrations\\2019_08_24_101751_add_design_updates.php",
        ".\database\migrations\\2019_09_02_101303_drop_images_character_foreign_key.php",
        ".\database\migrations\\2019_09_08_060400_drop_character_images_foreign_keys.php",
        ".\database\migrations\\2019_09_08_063923_add_submitted_at_to_design_updates.php",
        ".\database\migrations\\2019_09_17_110010_rename_design_approval_status.php",
        ".\database\migrations\\2019_09_28_040911_create_shops.php",
        ".\database\migrations\\2019_10_02_085738_add_shop_purchase_limits.php",
        ".\database\migrations\\2019_10_12_095632_add_bans.php",
        ".\database\migrations\\2019_10_21_081343_add_secure_trades.php",
        ".\database\migrations\\2019_11_05_062623_modify_trade_confirmation_flags.php",
        ".\database\migrations\\2019_12_02_090542_add_staff_id_to_trades.php",
        ".\database\migrations\\2019_12_23_062730_add_item_tags.php",
        ".\database\migrations\\2020_02_23_135512_make_prompt_category_nullable.php",
        ".\database\migrations\\2020_03_07_065050_add_bookmarks.php",
        ".\database\migrations\\2020_03_14_090241_make_character_log_sender_nullable.php",
        ".\database\migrations\\2020_03_14_124534_add_subtypes.php",
        ".\database\migrations\\2020_03_27_113928_add_subtype_to_features.php",
        ".\database\migrations\\2020_04_25_114747_drop_log_foreign_keys.php",
        ".\database\migrations\\2020_05_02_152118_drop_character_myo_counts.php",
        ".\database\migrations\\2020_06_01_124250_add_parsed_submission_comments.php",
        ".\database\migrations\\2020_07_31_185640_add_type_to_design_updates.php",
        ".\database\migrations\\2020_07_31_193235_set_design_update_type_null.php",
        ".\database\migrations\\2020_10_30_170108_add_gift_writing_status_to_characters.php",
        ".\database\migrations\\2020_11_09_201534_add_user_id_to_character_image_creators.php",
        ".\database\migrations\\2019_04_14_121447_add_transfer_flag_to_items.php",
        ".\database\migrations\\2019_04_14_120732_add_image_to_item_categories.php"
        
    ];
    
    for f in filePaths:
        sys.stdout.write("\r" + (" " * os.get_terminal_size().columns))
        sys.stdout.flush()
        sys.stdout.write("\r" + f)
        sys.stdout.flush()
        
        if os.path.exists(f):
            os.remove(f)
    

def findReplace():
    
    for filepath in glob.iglob('./**/*.php', recursive=True):
        if "vendor" not in filepath:
            sys.stdout.write("\r" + (" " * os.get_terminal_size().columns))
            sys.stdout.flush()
            sys.stdout.write("\r" + filepath)
            sys.stdout.flush()
            with open(filepath, encoding="utf8") as file:
                s = file.read()
            
                # various use statements
                s = s.replace('use DB;', 'use Illuminate\\Support\\Facades\\DB;')
                s = s.replace('use Auth;', 'use Illuminate\\Support\\Facades\Auth;')
                s = s.replace('use Notifications;', 'use App\\Facades\\Notifications;')
                s = s.replace('use Config;', 'use Illuminate\\Support\\Facades\\Config;')
                s = s.replace('use Image;', 'use Intervention\\Image\\Facades\\Image;')
                s = s.replace('use Settings;', 'use App\\Facades\\Settings;')
                s = s.replace('use App\Models\Comment;', 'use App\\Models\\Comment\\Comment;')
                s = s.replace("use File;", "use Illuminate\\Support\\Facades\\File;")
                
                # use classes instead of model string... obviously we can't cover every circumstance but this will help a lot
                # this doesn't add the respective use statement but it'll be added by the v3 merge
                s = s.replace("hasMany('App\\Models\\Character\\Character'", "hasMany(Character::class")
                s = s.replace("hasOne('App\\Models\\Character\\Character'", "hasOne(Character::class")
                s = s.replace("belongsTo('App\Models\Character\Character'", "belongsTo(Character::class")
                s = s.replace("belongsTo('App\\Models\\User\\User'", "belongsTo(User::class")
                s = s.replace("belongsTo('App\\Models\\Item\\Item'", "belongsTo(Item::class")
                s = s.replace("belongsTo('App\\Models\\Raffle\\Raffle'", "belongsTo(Raffle::class")
                s = s.replace("belongsTo('App\\Models\\Currency\\Currency'", "belongsTo(Currency::class")
                s = s.replace("belongsTo('App\Models\Shop\Shop'", "belongsTo(Shop::class")
                s = s.replace("hasMany('App\\Models\\Feature\\Feature'", "hasMany(Feature::class")
                s = s.replace("belongsTo('App\\Models\\Species\\Species'", "belongsTo(Species::class")
                
                # conversions
                s = s.replace('orderByRaw(DB::raw(', 'orderBy(DB::raw(')
                s = s.replace('Config::get(', 'config(')
                s = s.replace("return $this->id.'-image.png';", "return $this->hash.$this->id.'-image.png';")
                s = s.replace('return new $class;', 'return new $class();')
                
                # lang conversions
                s = s.replace("'.ucfirst(__('lorekeeper.subtype')).'", "Subtype")
                s = s.replace("'.__('lorekeeper.subtypes').'", "subtypes")
                s = s.replace("'.__('lorekeeper.subtype').'", "subtype")
                s = s.replace("'.ucfirst(__('lorekeeper.species')).'", "Species")
                s = s.replace("'.__('lorekeeper.specieses').'", "specieses")
                s = s.replace("'.__('lorekeeper.species').'", "species")
                
                # kernel.php
                s = s.replace("=> Middleware\\", "=> \\App\\Http\\Middleware\\")
                s = s.replace("Middleware\\CheckForMaintenanceMode::class", "\\App\\Http\\Middleware\\CheckForMaintenanceMode::class")
                s = s.replace("Middleware\\ParsePostRequestFields::class", "\\App\\Http\\Middleware\\ParsePostRequestFields::class")
                s = s.replace("Middleware\TrustProxies::class", "\\App\\Http\\Middleware\\TrustProxies::class")
                s = s.replace("Middleware\\TrimStrings::class", "\\App\\Http\\Middleware\\TrimStrings::class")
                s = s.replace("Middleware\\EncryptCookies::class", "\\App\\Http\\Middleware\\EncryptCookies::class")
                s = s.replace("Middleware\\VerifyCsrfToken::class", "\\App\\Http\\Middleware\\VerifyCsrfToken::class")
                s = s.replace("Middleware\\Authenticate::class", "\\App\\Http\\Middleware\\Authenticate::class")
                
                # comments on functions
                #s = s.replace("", "")
                #s = s.replace("", "")
            
            with open(filepath, "w") as file:
                file.write(s)

def datesToCasts():
    for filepath in glob.iglob('./**/*.php', recursive=True):
        if "vendor" not in filepath:
            sys.stdout.write("\r" + (" " * os.get_terminal_size().columns))
            sys.stdout.flush()
            sys.stdout.write("\r" + filepath)
            sys.stdout.flush()
            with fileinput.input(files=[filepath], inplace=True) as f:
            
                for line in f:
               
                    if re.search(r'(.+)\$dates = (\[.+\]);$', line):
                        access = re.search(r'(.+)\$dates = (\[.+\]);$', line).group(1)
                        datesString = re.search(r'(.+)\$dates = (\[.+\]);$', line).group(2)
                        
                        dates = literal_eval(datesString)
                        
                        newString = access + " $casts = [ "
                        for date in dates:
                            newString += "'" + date + "' => 'datetime', "
                        newString += "];"
                        
                    else:
                        newString = line
                        
                      # Modify the line as needed
                    print(newString, end='')        


# Define some common ANSI color codes
RESET = "\033[0m"
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

os.system('color')
width = os.get_terminal_size().columns 

print(YELLOW + ("~" * width) + RESET)
print(YELLOW + ("~" * (math.floor((width - 34)/2))) + RESET + " perappu's cool v3 upgrade script " + YELLOW + ("~" * (math.floor((width - 34)/2))) + RESET)
print(YELLOW + ("~" * width) + RESET)
print((RED + " WARNING! " + RESET + "This script automates a lot of destructive edits (deletes files, etc).").center(width))
print(YELLOW + ("~" * width) + RESET)

confirmation = input("- Have you already committed any important changes to git? ")

while confirmation != "yes":
    confirmation = input("Please type 'yes' to confirm, or ctrl+c to exit. ")
    
confirmation = input("- Have you run composer lint and the blade formatter? ")

while confirmation != "yes":
    confirmation = input("Please type 'yes' to confirm, or ctrl+c to exit. ")

print(YELLOW + ("~" * width) + RESET)
print((GREEN + " Let's go! " + RESET).center(width))
print(YELLOW + ("~" * width) + RESET)

print("- Deleting flattened migrations and other old files...")
print(BLUE)
deleteOldFiles()
print(RESET)
print()
print("- Finding and replacing common substitutions...")
print(BLUE)
findReplace()
print(RESET)
print()
print("- Fixing dates to casts...")
print(BLUE)
datesToCasts()
print(RESET)
print()
print(YELLOW + ("~" * width) + RESET)
print((GREEN + " All done! " + RESET).center(width))
print(YELLOW + ("~" * width) + RESET)
print(" Please run composer lint and the blade formatter an additional time before merging in V3. " + GREEN + "Good luck!" + RESET)