use std::io::{self, BufRead, Write, BufWriter};

fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let handle = stdout.lock();
    let mut writer = BufWriter::new(handle);

    for line in stdin.lock().lines().skip(1) {
        let line = line.unwrap();
        writeln!(writer, "Hello, {}!", line).expect("Failed to write to stdout");
    }
}
