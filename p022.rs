use std::fs::File;
use std::io::Read;

fn read_file() -> String {
    let mut file = File::open("p022.input").expect("Failed to open file");
    let mut file_content = String::new();
    file.read_to_string(&mut file_content).expect("Unable to read file");
    file_content
}

fn get_alphabetical_value(name: &str) -> usize {
    name.chars().map(|c| c as usize - 'A' as usize + 1).sum()
}

#[test]
fn test_get_alphabetical_value_example() {
    let actual = get_alphabetical_value("COLIN");
    assert_eq!(actual, 53, "COLIN is worth 3 + 15 + 12 + 9 + 14 = 53")
}

fn create_names_vec(file_content: &str) -> Vec<&str> {
    file_content
        .trim_start_matches('"')
        .trim_end_matches('"')
        .split("\",\"")
        .collect()
}

#[test]
fn test_read_file() {
    let file_content = read_file();
    let names_vec: Vec<&str> = create_names_vec(&file_content);

    assert_eq!(names_vec[0], "MARY", "First name in the file");
    assert_eq!(names_vec[names_vec.len() - 1], "ALONSO", "Last name in the file");
}

fn main() {
    let file_content = read_file();
    let mut names_vec: Vec<&str> = create_names_vec(&file_content);
    names_vec.sort();
    let total_names_score: usize =
        names_vec
            .into_iter().enumerate()
            .map(|(index, name)| (index + 1) * get_alphabetical_value(name))
            .sum();
    println!("{}", total_names_score);
}