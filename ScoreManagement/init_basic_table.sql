BEGIN;
--
-- Create model AdmClass
--
CREATE TABLE `adm_class` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(10) NOT NULL UNIQUE);
--
-- Create model ClassRoom
--
CREATE TABLE `class_room` (`crno` varchar(128) NOT NULL PRIMARY KEY, `crtype` varchar(10) NOT NULL, `contain_num` integer NOT NULL);
--
-- Create model College
--
CREATE TABLE `college` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(128) NOT NULL UNIQUE, `short_name` varchar(128) NOT NULL UNIQUE);
--
-- Create model Course
--
CREATE TABLE `course` (`cno` varchar(9) NOT NULL PRIMARY KEY, `cname` varchar(128) NOT NULL);
--
-- Create model CourseForSelect
--
CREATE TABLE `course_for_select` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model CourseSelected
--
CREATE TABLE `course_selected` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);
--
-- Create model Major
--
CREATE TABLE `major` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `mname` varchar(128) NOT NULL UNIQUE, `short_name` varchar(10) NOT NULL UNIQUE, `gra_score` integer NOT NULL, `in_college_id` integer NOT NULL);
--
-- Create model MajorPlan
--
CREATE TABLE `major_plan` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `cproper` bool NOT NULL, `score` integer NOT NULL, `chour` integer NOT NULL, `grade` integer NOT NULL, `semester` bool NOT NULL, `cno_id` varchar(9) NOT NULL, `mno_id` integer NOT NULL);
--
-- Create model Student
--
CREATE TABLE `student` (`user_ptr_id` integer NOT NULL UNIQUE, `sno` varchar(10) NOT NULL PRIMARY KEY, `sex` bool NOT NULL, `score_got` integer NOT NULL, `in_year` integer NOT NULL, `in_cls_id` integer NOT NULL, `mname_id` integer NOT NULL);
--
-- Create model Teacher
--
CREATE TABLE `teacher` (`user_ptr_id` integer NOT NULL UNIQUE, `tno` varchar(10) NOT NULL PRIMARY KEY, `sex` bool NOT NULL, `in_year` integer NOT NULL, `edu_background` varchar(128) NULL, `title` varchar(128) NOT NULL, `description` longtext NULL, `college_id` integer NOT NULL);
--
-- Create model Teaching
--
CREATE TABLE `teaching_table` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `weight` double precision NOT NULL, `mpno_id` integer NOT NULL, `tno_id` varchar(10) NOT NULL);
--
-- Add field college to course
--
ALTER TABLE `course` ADD COLUMN `college_id` integer NOT NULL;
--
-- Add field major to admclass
--
ALTER TABLE `adm_class` ADD COLUMN `major_id` integer NOT NULL;
--
-- Alter unique_together for teaching (1 constraint(s))
--
ALTER TABLE `teaching_table` ADD CONSTRAINT `teaching_table_tno_id_mpno_id_050e4d3f_uniq` UNIQUE (`tno_id`, `mpno_id`);
--
-- Alter unique_together for majorplan (1 constraint(s))
--
ALTER TABLE `major_plan` ADD CONSTRAINT `major_plan_cno_id_mno_id_cproper_sc_0878af48_uniq` UNIQUE (`cno_id`, `mno_id`, `cproper`, `score`, `chour`, `grade`, `semester`);
ALTER TABLE `major` ADD CONSTRAINT `major_in_college_id_19d3b0b6_fk_college_id` FOREIGN KEY (`in_college_id`) REFERENCES `college` (`id`);
ALTER TABLE `major_plan` ADD CONSTRAINT `major_plan_cno_id_f196f360_fk_course_cno` FOREIGN KEY (`cno_id`) REFERENCES `course` (`cno`);
ALTER TABLE `major_plan` ADD CONSTRAINT `major_plan_mno_id_0d92566b_fk_major_id` FOREIGN KEY (`mno_id`) REFERENCES `major` (`id`);
ALTER TABLE `student` ADD CONSTRAINT `student_user_ptr_id_44865c21_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `student` ADD CONSTRAINT `student_in_cls_id_eddc80d3_fk_adm_class_id` FOREIGN KEY (`in_cls_id`) REFERENCES `adm_class` (`id`);
ALTER TABLE `student` ADD CONSTRAINT `student_mname_id_3452dde7_fk_major_id` FOREIGN KEY (`mname_id`) REFERENCES `major` (`id`);
ALTER TABLE `teacher` ADD CONSTRAINT `teacher_user_ptr_id_d6fc1667_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `teacher` ADD CONSTRAINT `teacher_college_id_e9e59ee9_fk_college_id` FOREIGN KEY (`college_id`) REFERENCES `college` (`id`);
ALTER TABLE `teaching_table` ADD CONSTRAINT `teaching_table_mpno_id_e929dfcc_fk_major_plan_id` FOREIGN KEY (`mpno_id`) REFERENCES `major_plan` (`id`);
ALTER TABLE `teaching_table` ADD CONSTRAINT `teaching_table_tno_id_89c5ebe0_fk_teacher_tno` FOREIGN KEY (`tno_id`) REFERENCES `teacher` (`tno`);
ALTER TABLE `course` ADD CONSTRAINT `course_college_id_601395bf_fk_major_id` FOREIGN KEY (`college_id`) REFERENCES `major` (`id`);
ALTER TABLE `adm_class` ADD CONSTRAINT `adm_class_major_id_edbaa41c_fk_major_id` FOREIGN KEY (`major_id`) REFERENCES `major` (`id`);
COMMIT;
