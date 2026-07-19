# API Reliability Monitor — SLA Report

> Last updated: **2026-07-19 21:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.25% | 1977.2 | 10206.7 | 1000ms | 267/1504 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.6 | 4595.4 | 1500ms | 4/1504 |
| ❌ | `ipapi_check` | 72.67% | 99.93% | 152.5 | 4507.0 | 2500ms | 1/1504 |
| ❌ | `nasa_apod` | 76.46% | 52.33% | 3140.8 | 11152.5 | 2000ms | 717/1504 |
| ⚠️ | `dog_ceo_random` | 95.01% | 96.21% | 564.5 | 10244.1 | 2500ms | 57/1504 |
| ⚠️ | `open_meteo_weather` | 98.74% | 97.27% | 714.0 | 14877.1 | 2000ms | 41/1504 |
| ✅ | `rest_countries` | 99.0% | 98.74% | 303.0 | 10221.5 | 2500ms | 19/1504 |
| ✅ | `useless_fact` | 99.67% | 99.73% | 635.9 | 10229.6 | 2500ms | 4/1504 |
| ✅ | `catfact_random` | 99.8% | 99.4% | 255.4 | 10080.2 | 3000ms | 9/1504 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.7 | 4328.4 | 1500ms | 1/1504 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.9 | 16112.2 | 2000ms | 4/1504 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.1 | 3882.8 | 2000ms | 2/1504 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3891.8 | 50.79% |
| `nasa_apod` | 17:00 | 3842.7 | 52.56% |
| `nasa_apod` | 01:00 | 3614.7 | 52.17% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3496.8 | 51.19% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 18:00 | 3405.2 | 48.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
