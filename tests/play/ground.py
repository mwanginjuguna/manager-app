TABLES = {}

TABLES['logs'] = {
    "CREATE TABLE `logs`("
    " `id` int(11) NOT NULL AUTO_INCREMENT,"
    "`text` varchar(250) NOT NULL,"
    "`user` varchar(250) NOT NULL,"
    "`created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
}
