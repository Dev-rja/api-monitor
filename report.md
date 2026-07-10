# API Reliability Monitor — SLA Report

> Last updated: **2026-07-10 01:13 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.28% | 2169.1 | 10206.7 | 1000ms | 267/1354 |
| ❌ | `public_apis_list` | 0.0% | 99.7% | 122.4 | 4595.4 | 1500ms | 4/1354 |
| ❌ | `nasa_apod` | 74.67% | 50.3% | 3320.2 | 11152.5 | 2000ms | 673/1354 |
| ❌ | `ipapi_check` | 76.0% | 99.93% | 154.7 | 4507.0 | 2500ms | 1/1354 |
| ❌ | `dog_ceo_random` | 94.83% | 96.9% | 527.1 | 10244.1 | 2500ms | 42/1354 |
| ⚠️ | `open_meteo_weather` | 98.6% | 96.97% | 730.6 | 14877.1 | 2000ms | 41/1354 |
| ⚠️ | `rest_countries` | 98.89% | 98.6% | 316.2 | 10221.5 | 2500ms | 19/1354 |
| ✅ | `useless_fact` | 99.63% | 99.7% | 633.3 | 10229.6 | 2500ms | 4/1354 |
| ✅ | `catfact_random` | 99.78% | 99.34% | 255.7 | 10080.2 | 3000ms | 9/1354 |
| ✅ | `coingecko_bitcoin` | 99.78% | 99.93% | 97.9 | 4328.4 | 1500ms | 1/1354 |
| ✅ | `agify_name` | 99.93% | 99.7% | 384.2 | 16112.2 | 2000ms | 4/1354 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.85% | 211.5 | 3882.8 | 2000ms | 2/1354 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4792.7 | 80.95% |
| `nasa_apod` | 05:00 | 4162.5 | 60.53% |
| `nasa_apod` | 09:00 | 4153.2 | 53.45% |
| `nasa_apod` | 17:00 | 4069.4 | 55.71% |
| `numbers_trivia` | 03:00 | 4003.6 | 38.1% |
| `nasa_apod` | 01:00 | 3943.4 | 56.1% |
| `nasa_apod` | 18:00 | 3749.8 | 52.78% |
| `nasa_apod` | 11:00 | 3585.6 | 52.7% |
| `nasa_apod` | 20:00 | 3560.1 | 51.16% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
